"""
Django management command to add expert quiz questions
"""
from django.core.management.base import BaseCommand
from core.models import Question, Choice


class Command(BaseCommand):
    help = '전문가 모드 질문 추가'

    def handle(self, *args, **options):
        # 기존 전문가 질문 삭제
        deleted = Question.objects.filter(is_expert=True).delete()
        self.stdout.write(f'기존 전문가 질문 {deleted[0]}개 삭제')

        # Q1
        q1 = Question.objects.create(text="커피에서 산미가 분명하게 느껴질수록 매력적이라고 생각한다.", order=1, is_expert=True)
        Choice.objects.create(question=q1, text="매우 그렇다", acidity_score=3, body_score=0, sweetness_score=0, bitterness_score=0, aroma_score=1, aftertaste_score=0)
        Choice.objects.create(question=q1, text="그렇다", acidity_score=2, body_score=0, sweetness_score=0, bitterness_score=0, aroma_score=1, aftertaste_score=0)
        Choice.objects.create(question=q1, text="보통이다", acidity_score=1, body_score=1, sweetness_score=1, bitterness_score=1, aroma_score=1, aftertaste_score=1)
        Choice.objects.create(question=q1, text="아니다", acidity_score=0, body_score=1, sweetness_score=1, bitterness_score=2, aroma_score=0, aftertaste_score=1)
        Choice.objects.create(question=q1, text="전혀 아니다", acidity_score=0, body_score=2, sweetness_score=1, bitterness_score=3, aroma_score=0, aftertaste_score=2)

        # Q2
        q2 = Question.objects.create(text="과일이나 꽃 같은 밝은 향미가 또렷한 커피를 선호한다.", order=2, is_expert=True)
        Choice.objects.create(question=q2, text="매우 그렇다", acidity_score=2, body_score=0, sweetness_score=1, bitterness_score=0, aroma_score=3, aftertaste_score=0)
        Choice.objects.create(question=q2, text="그렇다", acidity_score=2, body_score=0, sweetness_score=1, bitterness_score=0, aroma_score=2, aftertaste_score=0)
        Choice.objects.create(question=q2, text="보통이다", acidity_score=1, body_score=1, sweetness_score=1, bitterness_score=1, aroma_score=1, aftertaste_score=1)
        Choice.objects.create(question=q2, text="아니다", acidity_score=0, body_score=1, sweetness_score=1, bitterness_score=1, aroma_score=1, aftertaste_score=1)
        Choice.objects.create(question=q2, text="전혀 아니다", acidity_score=0, body_score=2, sweetness_score=1, bitterness_score=2, aroma_score=0, aftertaste_score=2)

        # Q3
        q3 = Question.objects.create(text="쓴맛이 커피의 전체 인상을 단단하게 잡아준다고 느낀다.", order=3, is_expert=True)
        Choice.objects.create(question=q3, text="매우 그렇다", acidity_score=0, body_score=2, sweetness_score=0, bitterness_score=3, aroma_score=1, aftertaste_score=2)
        Choice.objects.create(question=q3, text="그렇다", acidity_score=0, body_score=1, sweetness_score=0, bitterness_score=2, aroma_score=1, aftertaste_score=1)
        Choice.objects.create(question=q3, text="보통이다", acidity_score=1, body_score=1, sweetness_score=1, bitterness_score=1, aroma_score=1, aftertaste_score=1)
        Choice.objects.create(question=q3, text="아니다", acidity_score=1, body_score=0, sweetness_score=2, bitterness_score=0, aroma_score=1, aftertaste_score=0)
        Choice.objects.create(question=q3, text="전혀 아니다", acidity_score=2, body_score=0, sweetness_score=2, bitterness_score=0, aroma_score=1, aftertaste_score=0)

        # Q4
        q4 = Question.objects.create(text="설탕이나 우유 없이도 블랙으로 마셨을 때 완성도가 높은 커피가 좋다.", order=4, is_expert=True)
        Choice.objects.create(question=q4, text="매우 그렇다", acidity_score=2, body_score=1, sweetness_score=0, bitterness_score=1, aroma_score=2, aftertaste_score=2)
        Choice.objects.create(question=q4, text="그렇다", acidity_score=1, body_score=1, sweetness_score=0, bitterness_score=1, aroma_score=1, aftertaste_score=1)
        Choice.objects.create(question=q4, text="보통이다", acidity_score=1, body_score=1, sweetness_score=1, bitterness_score=1, aroma_score=1, aftertaste_score=1)
        Choice.objects.create(question=q4, text="아니다", acidity_score=0, body_score=1, sweetness_score=2, bitterness_score=1, aroma_score=0, aftertaste_score=0)
        Choice.objects.create(question=q4, text="전혀 아니다", acidity_score=0, body_score=1, sweetness_score=3, bitterness_score=0, aroma_score=0, aftertaste_score=0)

        # Q5
        q5 = Question.objects.create(text="커피를 마셨을 때 입안에서 느껴지는 질감(바디감)이 중요하다.", order=5, is_expert=True)
        Choice.objects.create(question=q5, text="매우 그렇다", acidity_score=0, body_score=3, sweetness_score=1, bitterness_score=1, aroma_score=0, aftertaste_score=2)
        Choice.objects.create(question=q5, text="그렇다", acidity_score=0, body_score=2, sweetness_score=1, bitterness_score=1, aroma_score=0, aftertaste_score=1)
        Choice.objects.create(question=q5, text="보통이다", acidity_score=1, body_score=1, sweetness_score=1, bitterness_score=1, aroma_score=1, aftertaste_score=1)
        Choice.objects.create(question=q5, text="아니다", acidity_score=2, body_score=0, sweetness_score=1, bitterness_score=0, aroma_score=2, aftertaste_score=0)
        Choice.objects.create(question=q5, text="전혀 아니다", acidity_score=2, body_score=0, sweetness_score=1, bitterness_score=0, aroma_score=2, aftertaste_score=0)

        # Q6
        q6 = Question.objects.create(text="한 모금을 넘긴 뒤에도 맛과 향이 오래 남는 편이 좋다.", order=6, is_expert=True)
        Choice.objects.create(question=q6, text="매우 그렇다", acidity_score=0, body_score=2, sweetness_score=1, bitterness_score=1, aroma_score=2, aftertaste_score=3)
        Choice.objects.create(question=q6, text="그렇다", acidity_score=0, body_score=1, sweetness_score=1, bitterness_score=1, aroma_score=1, aftertaste_score=2)
        Choice.objects.create(question=q6, text="보통이다", acidity_score=1, body_score=1, sweetness_score=1, bitterness_score=1, aroma_score=1, aftertaste_score=1)
        Choice.objects.create(question=q6, text="아니다", acidity_score=2, body_score=0, sweetness_score=1, bitterness_score=0, aroma_score=1, aftertaste_score=0)
        Choice.objects.create(question=q6, text="전혀 아니다", acidity_score=2, body_score=0, sweetness_score=1, bitterness_score=0, aroma_score=1, aftertaste_score=0)

        # Q7
        q7 = Question.objects.create(text="초콜릿, 견과류, 카라멜 같은 단맛의 뉘앙스가 느껴지는 커피를 좋아한다.", order=7, is_expert=True)
        Choice.objects.create(question=q7, text="매우 그렇다", acidity_score=0, body_score=2, sweetness_score=3, bitterness_score=1, aroma_score=2, aftertaste_score=2)
        Choice.objects.create(question=q7, text="그렇다", acidity_score=0, body_score=1, sweetness_score=2, bitterness_score=1, aroma_score=1, aftertaste_score=1)
        Choice.objects.create(question=q7, text="보통이다", acidity_score=1, body_score=1, sweetness_score=1, bitterness_score=1, aroma_score=1, aftertaste_score=1)
        Choice.objects.create(question=q7, text="아니다", acidity_score=2, body_score=0, sweetness_score=0, bitterness_score=1, aroma_score=2, aftertaste_score=0)
        Choice.objects.create(question=q7, text="전혀 아니다", acidity_score=2, body_score=0, sweetness_score=0, bitterness_score=2, aroma_score=2, aftertaste_score=0)

        # Q8
        q8 = Question.objects.create(text="특정 맛이 튀기보다 전체적으로 균형 잡힌 커피가 가장 편하게 느껴진다.", order=8, is_expert=True)
        Choice.objects.create(question=q8, text="매우 그렇다", acidity_score=1, body_score=1, sweetness_score=1, bitterness_score=1, aroma_score=1, aftertaste_score=1)
        Choice.objects.create(question=q8, text="그렇다", acidity_score=1, body_score=1, sweetness_score=1, bitterness_score=1, aroma_score=1, aftertaste_score=1)
        Choice.objects.create(question=q8, text="보통이다", acidity_score=1, body_score=1, sweetness_score=1, bitterness_score=1, aroma_score=1, aftertaste_score=1)
        Choice.objects.create(question=q8, text="아니다", acidity_score=2, body_score=1, sweetness_score=0, bitterness_score=1, aroma_score=2, aftertaste_score=1)
        Choice.objects.create(question=q8, text="전혀 아니다", acidity_score=2, body_score=1, sweetness_score=0, bitterness_score=2, aroma_score=2, aftertaste_score=1)

        # Q9
        q9 = Question.objects.create(text="진한 커피가 오히려 부담 없이 안정적으로 느껴진다.", order=9, is_expert=True)
        Choice.objects.create(question=q9, text="매우 그렇다", acidity_score=0, body_score=3, sweetness_score=1, bitterness_score=2, aroma_score=1, aftertaste_score=2)
        Choice.objects.create(question=q9, text="그렇다", acidity_score=0, body_score=2, sweetness_score=1, bitterness_score=2, aroma_score=1, aftertaste_score=1)
        Choice.objects.create(question=q9, text="보통이다", acidity_score=1, body_score=1, sweetness_score=1, bitterness_score=1, aroma_score=1, aftertaste_score=1)
        Choice.objects.create(question=q9, text="아니다", acidity_score=2, body_score=0, sweetness_score=1, bitterness_score=0, aroma_score=1, aftertaste_score=0)
        Choice.objects.create(question=q9, text="전혀 아니다", acidity_score=2, body_score=0, sweetness_score=1, bitterness_score=0, aroma_score=2, aftertaste_score=0)

        # Q10
        q10 = Question.objects.create(text="커피를 마신 뒤 입안이 깔끔하게 정리되는 느낌을 중요하게 여긴다.", order=10, is_expert=True)
        Choice.objects.create(question=q10, text="매우 그렇다", acidity_score=2, body_score=0, sweetness_score=1, bitterness_score=0, aroma_score=1, aftertaste_score=0)
        Choice.objects.create(question=q10, text="그렇다", acidity_score=2, body_score=0, sweetness_score=1, bitterness_score=0, aroma_score=1, aftertaste_score=1)
        Choice.objects.create(question=q10, text="보통이다", acidity_score=1, body_score=1, sweetness_score=1, bitterness_score=1, aroma_score=1, aftertaste_score=1)
        Choice.objects.create(question=q10, text="아니다", acidity_score=0, body_score=2, sweetness_score=1, bitterness_score=1, aroma_score=1, aftertaste_score=2)
        Choice.objects.create(question=q10, text="전혀 아니다", acidity_score=0, body_score=2, sweetness_score=1, bitterness_score=2, aroma_score=1, aftertaste_score=3)

        count = Question.objects.filter(is_expert=True).count()
        self.stdout.write(self.style.SUCCESS(f'✅ 전문가 모드 질문 {count}개 추가 완료!'))
        
        for q in Question.objects.filter(is_expert=True).order_by('order'):
            self.stdout.write(f'  Q{q.order}. {q.text} ({q.choices.count()}개 선택지)')
