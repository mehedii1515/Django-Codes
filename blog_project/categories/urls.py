from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('add/',views.add_category, name = 'add_category')
]