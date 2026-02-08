import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffee_service.settings')
django.setup()

from core.models import Question

# Check current questions
questions = Question.objects.all().order_by('order')
print(f"Total questions: {questions.count()}\n")

for q in questions:
    print(f"{q.order}. {q.text}")
    for choice in q.choices.all():
        print(f"   - {choice.text}")
    print()
