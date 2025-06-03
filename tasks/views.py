from django.shortcuts import render
from .models import Tasks

# Create your views here.
def displayTask(request):
    tasklist = Tasks.objects.all()
    return render(request,'home.html',{"tasklist": tasklist})

def AddTask(request):
    return render(request,'AddTask.html')

def DeleteTask(request,task_id):
    return render(request,'EditTask.html',id=task_id)

def EditTask(request,task_id):
    return render(request,'EditTask.html',id=task_id)