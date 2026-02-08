@echo off
echo Adding expert quiz questions...
python -c "import os, django; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings'); django.setup(); exec(open('add_expert_questions_direct.py').read())"
echo.
echo Done!
pause
