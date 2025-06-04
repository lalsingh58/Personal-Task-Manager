from django.shortcuts import render,redirect
from .models import Tasks
from .forms import Taskform
from django.shortcuts import get_object_or_404

# Create your views here.
def displayTask(request):
    tasklist = Tasks.objects.all()
    return render(request,'home.html',{"tasklist": tasklist})

def AddTask(request):
    if(request.method == 'POST'):
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Taskform()
    return render(request,'AddTask.html',{'form':form})


def DeleteTask(request,task_id):
    task = get_object_or_404(Tasks,id=task_id)
    Tasks.delete(task)
    return redirect('home')
    



def EditTask(request,task_id):
    return render(request,'EditTask.html',id=task_id)