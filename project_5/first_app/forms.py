from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label= "User Name" , initial='Rahim', help_text='Enter your name',
    required= False, widget= forms.Textarea)
    # file = forms.FileField()
    email = forms.EmailField(label= "User Email")
    # age = forms.IntegerField(label= "Age")
    # weight = forms.FloatField()
    # balance = forms.DecimalField(label= 'Balance')
    age = forms.CharField(widget= forms.NumberInput)
    check = forms.BooleanField()
    birthday = forms.CharField(widget= forms.DateInput(attrs= {'type': 'date'}))
    appoinment = forms.CharField(widget= forms.DateInput(attrs= {'type': 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices= CHOICES, widget= forms.RadioSelect)
    meal = [('p', 'pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=meal, widget= forms.CheckboxSelectMultiple)
    
    
    
# class StudentData(forms.Form):
#     name= forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
    
#     def clean_name(self):
#         valname = self.cleaned_data['name']
#         if len(valname) < 10:
#             raise forms.ValidationError("Enter a name with atleast 10 characters")
#         return valname
    
    
    
class StudentData(forms.Form):
    name= forms.CharField(widget=forms.TextInput, validators= [validators.MaxLengthValidator(10, message= 'Enter a name with atleast 10 characters')])
    email = forms.CharField(widget=forms.EmailInput)
    age = forms.CharField()
    

class PasswordvalidationProject(forms.Form):
    name = forms.CharField(widget= forms.TextInput)
    password = forms.CharField(widget= forms.PasswordInput)
    confirm_password = forms.CharField(widget= forms.PasswordInput)
    
    
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['password']
        user_name = self.cleaned_data['name']
        if val_conpass != val_pass:
            raise forms.ValidationError("Password doesn't match")
        
        if len(user_name) < 15 :
            raise forms.ValidationError("User name must be atleast 15 cheracters")
        
        
class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_conpass != val_pass:
            raise forms.ValidationError("Password doesn't match")
        if len(val_name) < 15:
            raise forms.ValidationError("Name must be at least 15 characters")