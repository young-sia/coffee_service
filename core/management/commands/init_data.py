from django.core.management.base import BaseCommand
from core.models import Category, Question, Choice

class Command(BaseCommand):
    help = 'Initialize data for Coffee Hideout'

    def handle(self, *args, **kwargs):
        self.stdout.write('Initializing data...')

        # 1. Categories
        beverage, _ = Category.objects.get_or_create(name='Beverage')
        coffee, _ = Category.objects.get_or_create(name='Coffee', parent=beverage)
        americano, _ = Category.objects.get_or_create(name='Americano', parent=coffee)
        
        self.stdout.write(f'Created Categories: {beverage} > {coffee} > {americano}')

        # 2. Questions (Tarot Style)
        questions_data = [
            {
                "text": "1. 커피를 마실 때 가장 중요하게 생각하는 것은?",
                "order": 1,
                "choices": [
                    {"text": "상큼하고 깔끔한 맛 (산미)", "acidity": 2, "body": 0, "sweetness": 0},
                    {"text": "묵직하고 진한 느낌 (바디감)", "acidity": 0, "body": 2, "sweetness": 0},
                    {"text": "달콤하고 부드러운 향 (단맛/향)", "acidity": 0, "body": 0, "sweetness": 2},
                ]
            },
            {
                "text": "2. 어떤 과일을 좋아하시나요?",
                "order": 2,
                "choices": [
                    {"text": "레몬, 자몽 같은 시트러스류", "acidity": 2, "aroma": 1},
                    {"text": "다크 초콜릿, 견과류", "body": 2, "bitterness": 1},
                    {"text": "복숭아, 베리류", "sweetness": 2, "aroma": 1},
                ]
            },
            {
                "text": "3. 커피의 어떤 뒷맛을 선호하시나요?",
                "order": 3,
                "choices": [
                    {"text": "깔끔하게 사라지는 맛", "aftertaste": 0},
                    {"text": "오래 남는 여운", "aftertaste": 2},
                ]
            },
             {
                "text": "4. 평소 즐겨먹는 초콜릿 종류는?",
                "order": 4,
                "choices": [
                    {"text": "밀크 초콜릿", "sweetness": 2, "body": 1},
                    {"text": "다크 초콜릿 70% 이상", "bitterness": 2, "body": 2},
                    {"text": "화이트 초콜릿", "sweetness": 3, "body": 0},
                ]
            },
             {
                "text": "5. 커피를 주로 언제 마시나요?",
                "order": 5,
                "choices": [
                    {"text": "아침에 잠 깨려고 (강렬함)", "body": 2, "bitterness": 1},
                    {"text": "점심 식사 후 깔끔하게", "acidity": 1, "aftertaste": 1},
                    {"text": "휴식시간에 향을 즐기며", "aroma": 3},
                ]
            },
             {
                "text": "6. 선호하는 커피 농도는?",
                "order": 6,
                "choices": [
                    {"text": "연하게 물처럼", "body": -1},
                    {"text": "진하고 걸쭉하게", "body": 2},
                ]
            },
        ]

        if Question.objects.count() == 0:
            for q_data in questions_data:
                q = Question.objects.create(text=q_data["text"], order=q_data["order"])
                for c_data in q_data["choices"]:
                    Choice.objects.create(
                        question=q,
                        text=c_data["text"],
                        acidity_score=c_data.get("acidity", 0),
                        body_score=c_data.get("body", 0),
                        sweetness_score=c_data.get("sweetness", 0),
                        bitterness_score=c_data.get("bitterness", 0),
                        aroma_score=c_data.get("aroma", 0),
                        aftertaste_score=c_data.get("aftertaste", 0),
                    )
            self.stdout.write(f'Created {len(questions_data)} Questions')
        else:
            self.stdout.write('Questions already exist, skipping.')

        self.stdout.write(self.style.SUCCESS('Successfully initialized data'))
