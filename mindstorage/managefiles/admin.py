from django.contrib import admin

from .models import UserFile

# Register your models here.
@admin.register(UserFile)
class UserFileAdmin(admin.ModelAdmin):
    pass