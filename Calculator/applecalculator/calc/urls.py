from django.urls import path
from . import views
#from .views import home_view

urlpatterns = [
    path('', views.home, name='home'),
    #path('calculate/<str:operation>/', views.calculate, name='calculate'),
]
