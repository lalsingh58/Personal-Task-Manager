from django import forms
from .models import Tasks

class Taskform(forms.ModelForm):
    class Meta:
        model=Tasks
        fields = ('title','Task_name','task_due')