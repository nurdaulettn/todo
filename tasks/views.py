from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user).order_by('completed')
    else:
        tasks = ''
    context = {
        'tasks': tasks
    }

    return render(request, 'tasks/tasks.html', context)

@login_required
def add(request):
    if request.method=="POST":
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title, user=request.user)
    return redirect('index')

@login_required
def delete(request, pk):
    Task.objects.filter(id=pk).delete()
    return redirect('index')

@login_required
def complete(request, pk):
    task = Task.objects.get(id=pk)
    if task.completed:
        task.completed = False
    else:
        task.completed = True
    task.save()
    return redirect('index')

def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request,'tasks/register.html', {'form':form})