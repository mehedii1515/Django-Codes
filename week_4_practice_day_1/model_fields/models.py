from django.db import models

# Create your models here.
class TestModelForm(models.Model):
    phone = models.BigIntegerField() 
    agree = models.BooleanField()
    name = models.CharField(max_length=255)
    date = models.DateField()
    dateTime = models.DateTimeField()
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    email = models.EmailField() 
    file = models.FileField(upload_to='files/')
    float = models.FloatField()  
    ip_address = models.GenericIPAddressField()
    roll = models.IntegerField()
    null = models.BooleanField(null=True,blank=True) 
    student_id = models.SmallIntegerField() 
    massage = models.TextField()
    time = models.TimeField()
    url = models.URLField()
    uuid = models.UUIDField()
    fieldsets = [
        ('Main Information', {
            'fields': ('title', 'description')
        }),
        ('Additional Information', {
            'fields': ('slug', 'user', 'timestamp')
        }),
    ]