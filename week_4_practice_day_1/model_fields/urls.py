
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.model_fields, name='model_fields')
]