from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('add/',views.add_profile, name = 'add_profile')
]