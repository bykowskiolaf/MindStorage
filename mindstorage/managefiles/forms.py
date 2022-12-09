from django import forms

from .models import UserFile

# Form for adding files extending UserFile models
class AddFileForm(forms.ModelForm):
    class Meta:
        model = UserFile
        fields = ['file']

# Contact form
class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))