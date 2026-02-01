import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Item

def create_items():
    if Item.objects.exists():
        print("Data already exists. Skipping population.")
        return

    items = [
        {
            'name': 'Ethiopia Yirgacheffe',
            'category': 'COFFEE',
            'description': 'Floral and bright acidity with lemon notes.',
            'acidity': 8.5, 'body': 4.0, 'sweetness': 6.0, 'bitterness': 2.0, 'aroma': 9.0, 'texture': 5.0,
            'attributes': {'origin': 'Ethiopia', 'roast': 'Light'}
        },
        {
            'name': 'Colombia Supremo',
            'category': 'COFFEE',
            'description': 'Balanced body and acidity with nutty finish.',
            'acidity': 5.0, 'body': 7.0, 'sweetness': 6.5, 'bitterness': 4.0, 'aroma': 6.5, 'texture': 6.0,
            'attributes': {'origin': 'Colombia', 'roast': 'Medium'}
        },
        {
            'name': 'Earl Grey Tea',
            'category': 'TEA',
            'description': 'Black tea flavored with bergamot oil.',
            'acidity': 4.0, 'body': 3.0, 'sweetness': 4.0, 'bitterness': 5.0, 'aroma': 8.0, 'texture': 2.0,
            'attributes': {'type': 'Black', 'caffeine': 'High'}
        },
        {
            'name': 'New York Cheesecake',
            'category': 'FOOD',
            'description': 'Rich and creamy dessert.',
            'acidity': 2.0, 'body': 9.0, 'sweetness': 9.0, 'bitterness': 0.0, 'aroma': 5.0, 'texture': 9.0,
            'attributes': {'calories': 400}
        }
    ]

    for data in items:
        Item.objects.create(**data)
        print(f"Created: {data['name']}")

if __name__ == '__main__':
    create_items()
