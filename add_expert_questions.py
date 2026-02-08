import os
import django
import sys

# Django 설정
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from core.models import Question, Choice

# 전문가 모드 질문 추가
def add_expert_questions():
    print("전문가 모드 질문 추가 중...")
    
    # 기존 전문가 질문 삭제
    Question.objects.filter(is_expert=True).delete()
    
    # 전문가 질문 1: 산미 선호도
    q1 = Question.objects.create(
        text="커피의 산미(Acidity)에 대한 당신의 선호도는?",
        order=1,
        is_expert=True
    )
    Choice.objects.create(
        question=q1,
        text="밝고 생동감 있는 산미를 선호합니다",
        acidity_score=3, body_score=0, sweetness_score=1,
        bitterness_score=0, aroma_score=2, aftertaste_score=1
    )
    Choice.objects.create(
        question=q1,
        text="적당한 산미가 좋습니다",
        acidity_score=2, body_score=1, sweetness_score=1,
        bitterness_score=1, aroma_score=1, aftertaste_score=1
    )
    Choice.objects.create(
        question=q1,
        text="산미가 거의 없는 것을 선호합니다",
        acidity_score=0, body_score=2, sweetness_score=1,
        bitterness_score=2, aroma_score=1, aftertaste_score=2
    )
    
    # 전문가 질문 2: 바디감
    q2 = Question.objects.create(
        text="커피의 바디(Body)감에 대한 선호도는?",
        order=2,
        is_expert=True
    )
    Choice.objects.create(
        question=q2,
        text="묵직하고 크리미한 질감",
        acidity_score=0, body_score=3, sweetness_score=2,
        bitterness_score=2, aroma_score=1, aftertaste_score=2
    )
    Choice.objects.create(
        question=q2,
        text="중간 정도의 바디감",
        acidity_score=1, body_score=2, sweetness_score=1,
        bitterness_score=1, aroma_score=1, aftertaste_score=1
    )
    Choice.objects.create(
        question=q2,
        text="가볍고 깔끔한 질감",
        acidity_score=2, body_score=0, sweetness_score=1,
        bitterness_score=0, aroma_score=2, aftertaste_score=1
    )
    
    # 전문가 질문 3: 단맛
    q3 = Question.objects.create(
        text="커피의 단맛(Sweetness)에 대한 선호도는?",
        order=3,
        is_expert=True
    )
    Choice.objects.create(
        question=q3,
        text="캐러멜, 초콜릿 같은 풍부한 단맛",
        acidity_score=0, body_score=2, sweetness_score=3,
        bitterness_score=1, aroma_score=2, aftertaste_score=2
    )
    Choice.objects.create(
        question=q3,
        text="은은한 단맛",
        acidity_score=1, body_score=1, sweetness_score=2,
        bitterness_score=1, aroma_score=1, aftertaste_score=1
    )
    Choice.objects.create(
        question=q3,
        text="단맛보다는 쓴맛 위주",
        acidity_score=1, body_score=1, sweetness_score=0,
        bitterness_score=3, aroma_score=1, aftertaste_score=2
    )
    
    # 전문가 질문 4: 쓴맛
    q4 = Question.objects.create(
        text="커피의 쓴맛(Bitterness)에 대한 선호도는?",
        order=4,
        is_expert=True
    )
    Choice.objects.create(
        question=q4,
        text="강렬하고 진한 쓴맛",
        acidity_score=0, body_score=2, sweetness_score=0,
        bitterness_score=3, aroma_score=1, aftertaste_score=2
    )
    Choice.objects.create(
        question=q4,
        text="적당한 쓴맛",
        acidity_score=1, body_score=1, sweetness_score=1,
        bitterness_score=2, aroma_score=1, aftertaste_score=1
    )
    Choice.objects.create(
        question=q4,
        text="쓴맛이 적은 부드러운 커피",
        acidity_score=2, body_score=1, sweetness_score=2,
        bitterness_score=0, aroma_score=2, aftertaste_score=1
    )
    
    # 전문가 질문 5: 향
    q5 = Question.objects.create(
        text="커피의 향(Aroma)에 대한 선호도는?",
        order=5,
        is_expert=True
    )
    Choice.objects.create(
        question=q5,
        text="플로럴, 과일향이 풍부한 커피",
        acidity_score=3, body_score=0, sweetness_score=1,
        bitterness_score=0, aroma_score=3, aftertaste_score=1
    )
    Choice.objects.create(
        question=q5,
        text="견과류, 초콜릿 향",
        acidity_score=1, body_score=2, sweetness_score=2,
        bitterness_score=1, aroma_score=2, aftertaste_score=2
    )
    Choice.objects.create(
        question=q5,
        text="스모키, 로스티한 향",
        acidity_score=0, body_score=2, sweetness_score=1,
        bitterness_score=3, aroma_score=2, aftertaste_score=2
    )
    
    # 전문가 질문 6: 후미
    q6 = Question.objects.create(
        text="커피의 후미(Aftertaste)에 대한 선호도는?",
        order=6,
        is_expert=True
    )
    Choice.objects.create(
        question=q6,
        text="길고 복합적인 여운",
        acidity_score=1, body_score=2, sweetness_score=1,
        bitterness_score=2, aroma_score=2, aftertaste_score=3
    )
    Choice.objects.create(
        question=q6,
        text="적당한 여운",
        acidity_score=1, body_score=1, sweetness_score=1,
        bitterness_score=1, aroma_score=1, aftertaste_score=2
    )
    Choice.objects.create(
        question=q6,
        text="깔끔하고 짧은 여운",
        acidity_score=2, body_score=0, sweetness_score=1,
        bitterness_score=0, aroma_score=1, aftertaste_score=0
    )
    
    print(f"✅ 전문가 모드 질문 {Question.objects.filter(is_expert=True).count()}개 추가 완료!")

if __name__ == '__main__':
    add_expert_questions()
    
    # 확인
    print("\n=== 전문가 모드 질문 목록 ===")
    for q in Question.objects.filter(is_expert=True).order_by('order'):
        print(f"{q.order}. {q.text}")
        for c in q.choices.all():
            print(f"   - {c.text}")
