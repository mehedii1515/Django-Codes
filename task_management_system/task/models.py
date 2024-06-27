from django.db import models
from datetime import date
from category.models import Category

# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateField(default=date.today)
    
    
    def __str__(self):
        return self.task_title