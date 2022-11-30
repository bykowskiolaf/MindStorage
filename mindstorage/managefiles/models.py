from django.db import models

from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return f'{instance.owner.username}/{filename}'

# Create your models here.
class UserFile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path)
    uploaded = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    trash = models.BooleanField(default=False)
    favourite = models.BooleanField(default=False)
    