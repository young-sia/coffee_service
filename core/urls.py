from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/', views.quiz_view, name='quiz'),
    path('result/', views.quiz_result, name='quiz_result'),
    path('quiz/expert/', views.expert_quiz_view, name='expert_quiz'),
    path('result/expert/', views.expert_result, name='expert_result'),
    path('daily-recommendation/', views.daily_recommendation, name='daily_recommendation'),
    path('roulette/', views.roulette_page, name='roulette_page'),
    path('api/next-recommendation/', views.get_next_recommendation, name='next_recommendation'),
    path('api/roulette/', views.roulette_recommendation, name='roulette_recommendation'),
]
