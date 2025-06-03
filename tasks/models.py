from django.db import models

# Create your models here.
class Tasks(models.Model):
    title =  models.CharField(max_length=200)
    Task_name = models.TextField(max_length=1000)
    task_created =  models.DateTimeField(auto_now_add=True)
    task_updated = models.DateTimeField(auto_now=True)
    task_due = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title