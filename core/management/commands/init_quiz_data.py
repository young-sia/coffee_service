from django.core.management.base import BaseCommand
from core.models import Question, Choice

class Command(BaseCommand):
    help = 'Initialize quiz questions with natural language approach'

    def handle(self, *args, **kwargs):
        # Clear existing questions
        Question.objects.all().delete()
        
        # Natural Language Questions (6 questions)
        questions_data = [
            {
                'text': '아침에 눈을 떴을 때, 보통 어떤 편이에요?',
                'order': 1,
                'is_expert': False,
                'choices': [
                    {
                        'text': '바로 정신이 드는 편',
                        'scores': {'acidity': 3, 'body': 1, 'sweetness': 2, 'bitterness': 0, 'aroma': 2, 'aftertaste': 1}
                    },
                    {
                        'text': '멍한 시간이 조금 필요해요',
                        'scores': {'acidity': 0, 'body': 3, 'sweetness': 2, 'bitterness': 2, 'aroma': 2, 'aftertaste': 3}
                    },
                    {
                        'text': '그날그날 달라요',
                        'scores': {'acidity': 2, 'body': 2, 'sweetness': 2, 'bitterness': 1, 'aroma': 2, 'aftertaste': 2}
                    },
                ]
            },
            {
                'text': '음식이나 음료를 고를 때, 더 자주 끌리는 쪽은요?',
                'order': 2,
                'is_expert': False,
                'choices': [
                    {
                        'text': '상큼해서 계속 들어가는 맛',
                        'scores': {'acidity': 3, 'body': 1, 'sweetness': 2, 'bitterness': 0, 'aroma': 3, 'aftertaste': 1}
                    },
                    {
                        'text': '편안하고 익숙한 맛',
                        'scores': {'acidity': 1, 'body': 2, 'sweetness': 2, 'bitterness': 1, 'aroma': 2, 'aftertaste': 3}
                    },
                    {
                        'text': '달거나 진해서 만족감이 큰 맛',
                        'scores': {'acidity': 0, 'body': 3, 'sweetness': 3, 'bitterness': 2, 'aroma': 2, 'aftertaste': 3}
                    },
                ]
            },
            {
                'text': '카페에서 메뉴를 고를 때는 보통 어떤 편인가요?',
                'order': 3,
                'is_expert': False,
                'choices': [
                    {
                        'text': '늘 비슷한 걸 고르는 편',
                        'scores': {'acidity': 1, 'body': 2, 'sweetness': 2, 'bitterness': 1, 'aroma': 1, 'aftertaste': 3}
                    },
                    {
                        'text': '가끔 다른 걸 시도해봐요',
                        'scores': {'acidity': 2, 'body': 2, 'sweetness': 2, 'bitterness': 2, 'aroma': 2, 'aftertaste': 2}
                    },
                    {
                        'text': '새로운 게 있으면 한 번쯤은 꼭',
                        'scores': {'acidity': 3, 'body': 2, 'sweetness': 1, 'bitterness': 2, 'aroma': 3, 'aftertaste': 2}
                    },
                ]
            },
            {
                'text': '커피를 마시는 순간을 떠올리면 더 가까운 건요?',
                'order': 4,
                'is_expert': False,
                'choices': [
                    {
                        'text': '혼자 조용히 집중할 때',
                        'scores': {'acidity': 1, 'body': 3, 'sweetness': 1, 'bitterness': 2, 'aroma': 2, 'aftertaste': 3}
                    },
                    {
                        'text': '잠깐 쉬는 시간',
                        'scores': {'acidity': 2, 'body': 2, 'sweetness': 2, 'bitterness': 1, 'aroma': 2, 'aftertaste': 2}
                    },
                    {
                        'text': '사람들과 이야기하면서',
                        'scores': {'acidity': 3, 'body': 1, 'sweetness': 2, 'bitterness': 0, 'aroma': 3, 'aftertaste': 1}
                    },
                ]
            },
            {
                'text': '추천받은 메뉴가 생각과 달랐을 때는요?',
                'order': 5,
                'is_expert': False,
                'choices': [
                    {
                        'text': '다음엔 안 고를 것 같아요',
                        'scores': {'acidity': 1, 'body': 2, 'sweetness': 2, 'bitterness': 0, 'aroma': 1, 'aftertaste': 3}
                    },
                    {
                        'text': '그냥 그런 날도 있다고 생각해요',
                        'scores': {'acidity': 2, 'body': 2, 'sweetness': 2, 'bitterness': 1, 'aroma': 2, 'aftertaste': 2}
                    },
                    {
                        'text': '경험으로 받아들이는 편이에요',
                        'scores': {'acidity': 2, 'body': 2, 'sweetness': 1, 'bitterness': 3, 'aroma': 3, 'aftertaste': 2}
                    },
                ]
            },
            {
                'text': '커피를 마시고 나서 가장 좋게 느껴지는 순간은요?',
                'order': 6,
                'is_expert': False,
                'choices': [
                    {
                        'text': '맛이 또렷하게 느껴질 때',
                        'scores': {'acidity': 3, 'body': 2, 'sweetness': 1, 'bitterness': 3, 'aroma': 2, 'aftertaste': 2}
                    },
                    {
                        'text': '향이나 분위기가 좋을 때',
                        'scores': {'acidity': 2, 'body': 2, 'sweetness': 2, 'bitterness': 1, 'aroma': 3, 'aftertaste': 2}
                    },
                    {
                        'text': '마신 뒤 기분이 괜찮을 때',
                        'scores': {'acidity': 1, 'body': 2, 'sweetness': 2, 'bitterness': 1, 'aroma': 2, 'aftertaste': 3}
                    },
                ]
            },
        ]

        for q_data in questions_data:
            question = Question.objects.create(
                text=q_data['text'],
                order=q_data['order'],
                is_expert=q_data['is_expert'],
                question_type='multiple_choice'
            )
            
            for c_data in q_data['choices']:
                Choice.objects.create(
                    question=question,
                    text=c_data['text'],
                    acidity_score=c_data['scores']['acidity'],
                    body_score=c_data['scores']['body'],
                    sweetness_score=c_data['scores']['sweetness'],
                    bitterness_score=c_data['scores']['bitterness'],
                    aroma_score=c_data['scores']['aroma'],
                    aftertaste_score=c_data['scores']['aftertaste'],
                )
            
            self.stdout.write(self.style.SUCCESS(f'Created question: {question.text}'))

        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully created {len(questions_data)} natural language questions!'))
