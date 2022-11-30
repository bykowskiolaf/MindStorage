from django import forms

from .models import UserFile

class AddFileForm(forms.ModelForm):
    class Meta:
        model = UserFile
        fields = ['file']