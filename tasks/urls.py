from django.urls import path
from .views import *

urlpatterns = [
    path('',displayTask,name="home"),
    path('addtask/',AddTask,name="addtask"),
    path('deletetask/<int:task_id>',DeleteTask,name="deletetask"),
    path('edit/task/<int:task_id>',EditTask,name="edittask")
]
