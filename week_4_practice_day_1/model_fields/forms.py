from django import forms
from model_fields.models import TestModelForm

class TestModel(forms.ModelForm):
    class Meta:
        model = TestModelForm
        fields = "__all__" 
  