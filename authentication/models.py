from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Author(AbstractUser):
    bio = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self):
        return self.username