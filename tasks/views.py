from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request,'home.html')

def AddTask(request):
    return render(request,'AddTask.html')

def DeleteTask(request,task_id):
    return render(request,'EditTask.html',id=task_id)

def EditTask(request,task_id):
    return render(request,'EditTask.html',id=task_id)