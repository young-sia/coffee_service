from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return f"{self.parent} > {self.name}"
        return self.name

class FlavorProfile(models.Model):
    acidity = models.IntegerField(default=0)    # 산미
    body = models.IntegerField(default=0)       # 바디
    sweetness = models.IntegerField(default=0)  # 단맛
    bitterness = models.IntegerField(default=0) # 쓴맛
    aroma = models.IntegerField(default=0)      # 향
    aftertaste = models.IntegerField(default=0) # 후미

    def __str__(self):
        return f"A:{self.acidity} B:{self.body}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    flavor_profile = models.OneToOneField(FlavorProfile, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    QUESTION_TYPE_CHOICES = [
        ('multiple_choice', 'Multiple Choice'),
        ('scale', 'Scale (1-5)'),
        ('binary', 'Yes/No'),
    ]
    
    text = models.CharField(max_length=200)
    order = models.IntegerField()
    image = models.ImageField(upload_to='tarot_cards/', null=True, blank=True)
    is_expert = models.BooleanField(default=False)  # False = general user, True = expert mode
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE_CHOICES, default='multiple_choice')

    def __str__(self):
        mode = "Expert" if self.is_expert else "General"
        return f"[{mode}] {self.text}"

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    # Scores
    acidity_score = models.IntegerField(default=0)
    body_score = models.IntegerField(default=0)
    sweetness_score = models.IntegerField(default=0)
    bitterness_score = models.IntegerField(default=0)
    aroma_score = models.IntegerField(default=0)
    aftertaste_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.question.text} - {self.text}"

class UserTasteProfile(models.Model):
    user_session_id = models.CharField(max_length=100, null=True, blank=True) # For anonymous users
    # We could link to User model if we had login
    created_at = models.DateTimeField(auto_now_add=True)
    # Storing the result flavor profile
    flavor_profile = models.OneToOneField(FlavorProfile, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Profile {self.id} ({self.created_at})"
