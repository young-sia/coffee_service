from django.core.management.base import BaseCommand
from core.models import Category, Product, FlavorProfile

class Command(BaseCommand):
    help = 'Initialize dummy products'

    def handle(self, *args, **kwargs):
        self.stdout.write('Initializing products...')

        try:
            coffee = Category.objects.get(name='Coffee')
        except Category.DoesNotExist:
            self.stdout.write(self.style.ERROR('Run init_data first!'))
            return

        products_data = [
            {
                "name": "에티오피아 예가체프",
                "desc": "꽃향기와 상큼한 산미가 특징인 커피",
                "flavor": {"acidity": 5, "body": 2, "sweetness": 4, "bitterness": 1, "aroma": 5, "aftertaste": 4}
            },
            {
                "name": "과테말라 안티구아",
                "desc": "스모키한 향과 묵직한 바디감",
                "flavor": {"acidity": 2, "body": 4, "sweetness": 3, "bitterness": 3, "aroma": 3, "aftertaste": 3}
            },
            {
                "name": "케냐 AA",
                "desc": "강렬한 산미와 무거운 바디감의 조화",
                "flavor": {"acidity": 4, "body": 4, "sweetness": 3, "bitterness": 2, "aroma": 4, "aftertaste": 4}
            },
            {
                "name": "브라질 산토스",
                "desc": "부드러운 맛과 고소함, 낮은 산미",
                "flavor": {"acidity": 1, "body": 3, "sweetness": 2, "bitterness": 2, "aroma": 2, "aftertaste": 2}
            },
            {
                "name": "인도네시아 만델링",
                "desc": "진한 쓴맛과 묵직한 바디감, 남성적인 커피",
                "flavor": {"acidity": 1, "body": 5, "sweetness": 2, "bitterness": 5, "aroma": 3, "aftertaste": 5}
            },
        ]

        for p_data in products_data:
            fp, _ = FlavorProfile.objects.get_or_create(**p_data["flavor"])
            Product.objects.get_or_create(
                name=p_data["name"],
                category=coffee,
                defaults={
                    "description": p_data["desc"],
                    "flavor_profile": fp
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully initialized products'))
