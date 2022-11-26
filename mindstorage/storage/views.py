from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import Upload

from .models import Plik

def home(request):
    return render(request, 'storage/home.html')

@login_required
def dashboard(request):
    all_files = Plik.objects.filter(owner=request.user)
    if request.method == 'POST':
        upload_file = Upload(request.POST,request.FILES)
        if upload_file.is_valid():
            plik = upload_file.save(commit=False)
            plik.owner = request.user
            plik.save()
    else:
        upload_file = Upload()
    return render(request,
                  'storage/dashboard.html',
                  {'form': upload_file,
                   'all_files': all_files,})

