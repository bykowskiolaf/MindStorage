from django.contrib import admin

from .models import Plik

@admin.register(Plik)
class Plik(admin.ModelAdmin):
    pass