from django.shortcuts import render

# Create your views here.
def filter(request):
    return render(request,"filter.html")