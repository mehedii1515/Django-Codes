from django import forms
import datetime
from django.forms.widgets import NumberInput
# Create your forms here.

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class ExampleForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3})) 
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField()
    value = forms.DecimalField()
    first_name = forms.CharField(initial='Your name')
    day = forms.DateField(initial=datetime.date.today)
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    
    