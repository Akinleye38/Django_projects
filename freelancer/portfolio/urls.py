from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('pricing/', views.pricing, name='pricing'),
    path('blog/', views.blog, name='blog'),
    path('case_studies/', views.case_studies, name='case_studies'),
]