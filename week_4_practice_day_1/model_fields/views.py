# from django.shortcuts import render

# # Create your views here.
# def model_fields(request):
#     return render(request,'model_fields.html')

from django.shortcuts import render
from model_fields.forms import TestModel
# Create your views here.
def model_fields(request):
    if request.method == 'POST':
        form = TestModel(request.POST)
        if form.is_valid():
            form = TestModel()
    else:
        form = TestModel()
    return render(request,'model_fields.html',{'form':form})

  