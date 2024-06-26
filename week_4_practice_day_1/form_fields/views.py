from django.shortcuts import render, redirect
from . import forms
# Create your views here.


def form_fields(request):
    if request.method == 'POST':
        form_field = forms.ExampleForm(request.POST)
        if form_field.is_valid():
            form_field = form_fields()
            
    else:
        form_field = forms.ExampleForm()

    return render(request, 'form_fields.html', {'form': form_field})
