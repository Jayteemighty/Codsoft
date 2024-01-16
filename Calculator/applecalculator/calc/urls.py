# calc/urls.py
from django.urls import path
from .views import home, calculate

urlpatterns = [
    path('home/', home, name='home'),
    path('calculate/<str:operation>/', calculate, name='calculate'),
]
