from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('journey/', views.coffee_journey, name='coffee_journey'),
    path('analysis/', views.preference_form, name='preference_form'),
    path('recommend/', views.recommend, name='recommend'),
]
