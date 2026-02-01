from django.db import models
from django.contrib.auth.models import User

class FlavorVectorMixin(models.Model):
    """
    Mixin to provide specific flavor vectors for analysis (Scikit-learn).
    Normalized to 0.0 - 10.0 scale.
    """
    acidity = models.FloatField(default=0.0, help_text="Acidic taste (0-10)")
    body = models.FloatField(default=0.0, help_text="Body/Weight (0-10)")
    sweetness = models.FloatField(default=0.0, help_text="Sweetness (0-10)")
    bitterness = models.FloatField(default=0.0, help_text="Bitterness (0-10)")
    aroma = models.FloatField(default=0.0, help_text="Aroma intensity (0-10)")
    texture = models.FloatField(default=0.0, help_text="Texture/Carbonation (0-10)")
    caffeine = models.FloatField(default=0.0, help_text="Caffeine content (mg or relative scale)")

    class Meta:
        abstract = True

    def get_vector(self):
        """Returns the feature vector list [acidity, body, sweetness, bitterness, aroma, texture, caffeine]"""
        return [
            self.acidity,
            self.body,
            self.sweetness,
            self.bitterness,
            self.aroma,
            self.texture,
            self.caffeine
        ]

class Item(FlavorVectorMixin):
    CATEGORY_CHOICES = [
        ('COFFEE', 'Coffee'),
        ('TEA', 'Tea'),
        ('FOOD', 'Food'),
        ('BEVERAGE', 'Other Beverage'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='COFFEE')
    description = models.TextField(blank=True)
    
    # Flexible container for category-specific attributes (e.g., origin, roast_level, calories)
    attributes = models.JSONField(default=dict, blank=True)
    
    def __str__(self):
        return f"[{self.get_category_display()}] {self.name}"

class UserPreference(FlavorVectorMixin):
    """
    Stores the user's LONG-TERM baseline preference.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='preference')
    
    def __str__(self):
        return f"{self.user.username}'s Preference"
