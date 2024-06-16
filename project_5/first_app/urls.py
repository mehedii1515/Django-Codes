from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('form/', views.form, name = 'form'),
    path('about/', views.about, name = 'about'),
    path('django_form/', views.django_form, name = 'django_form'),
    path('StudentForm/', views.PasswordValidation, name = 'StudentForm'),
]