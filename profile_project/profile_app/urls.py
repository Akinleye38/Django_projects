from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('hobbies/', views.hobbies, name= 'hobbies'),
    path('goals/', views.goals, name= 'goals'),
]