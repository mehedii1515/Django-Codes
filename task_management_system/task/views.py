from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
# Add Task Functions:
def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
    
    else:
        task_form = forms.TaskForm()
    return render(request, 'task.html', {'form' : task_form})

# Edit Task Functions:
def edit_task(request, id):
    task = models.Task.objects.get(pk=id)
    task_form = forms.TaskForm(instance=task)
    # print(post.title)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('homepage')
    return render(request, 'task.html', {'form' : task_form})

# Delete Task Functions:
def delete_task(request, id):
    task = models.Task.objects.get(pk=id) 
    task.delete()
    return redirect('homepage')