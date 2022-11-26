from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/media/author/<filename>
    return f'{instance.owner}/{filename}'

class Plik(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    plik = models.FileField(upload_to=user_directory_path)
    upload_date = models.DateTimeField(auto_now=True)