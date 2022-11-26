from django.forms import ModelForm

from .models import Plik

class Upload(ModelForm):
    class Meta:
        model = Plik
        fields = ['plik']