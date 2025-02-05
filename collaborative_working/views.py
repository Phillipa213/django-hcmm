from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from .models import CollaborativeTask
from .forms import CollaborativeTaskForm

# In views.py
from django.shortcuts import render

def home(request):
    tasks = CollaborativeTask.objects.all()
    return render(request, 'collaborative_working/home.html', {'tasks': tasks})


def task_list(request):
    tasks = CollaborativeTask.objects.all()
    return render(request, 'collaborative_working/list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(CollaborativeTask, pk=pk)
    return render(request, 'collaborative_working/detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = CollaborativeTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('collaborative_working:task_list')
    else:
        form = CollaborativeTaskForm()
    return render(request, 'collaborative_working/form.html', {'form': form})

# Add Task View
def add_task(request):
    if request.method == "POST":
        form = CollaborativeTaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task added successfully!")
            return redirect('collaborative_working:home')
    else:
        form = CollaborativeTaskForm()

    return render(request, 'collaborative_working/add_task.html', {'form': form})

# Update Task View
def update_task(request, pk):
    task = get_object_or_404(CollaborativeTask, pk=pk)
    if request.method == "POST":
        form = CollaborativeTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect('collaborative_working:home')
    else:
        form = CollaborativeTaskForm(instance=task)

    return render(request, 'collaborative_working/update_task.html', {'form': form, 'task': task})

# Delete Task Confirmation View
def delete_task(request, pk):
    task = get_object_or_404(CollaborativeTask, pk=pk)
    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted successfully!")
        return redirect('collaborative_working:home')

    return render(request, 'collaborative_working/delete_task.html', {'task': task})