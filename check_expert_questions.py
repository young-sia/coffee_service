import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from core.models import Question

# 전문가 질문 확인
expert_questions = Question.objects.filter(is_expert=True).order_by('order')
count = expert_questions.count()

print(f"전문가 모드 질문 개수: {count}개")
print("\n=== 전문가 모드 질문 목록 ===")
for q in expert_questions:
    print(f"Q{q.order}. {q.text}")
    print(f"   선택지 개수: {q.choices.count()}개")

if count == 0:
    print("\n⚠️ 전문가 질문이 없습니다!")
    print("run_expert_questions.bat 파일을 실행해주세요.")
