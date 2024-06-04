from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d = {'author': 'rahim', 'age': '25', 'lst': ['python',"is","best"], 'birthday': datetime.datetime.now,'val':" ", 'courses': [
        {
            'id': 1,
            'name': 'Python',
            'fee': 4000,
        },
        {
            'id': 2,
            'name': 'Django',
            'fee': 5500,
        },
        {
            'id': 3,
            'name': 'C',
            'fee': 1000,
        },
        
        ]}
    return render(request, 'home.html', d)