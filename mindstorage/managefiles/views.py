from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render ,get_object_or_404, redirect

from .models import UserFile

from .forms import AddFileForm, ContactForm

def welcome_screen(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            send_mail(subject, message, from_email, ["admin@example.com"])
            return redirect('managefiles:welcome_screen')
    return render(request, 'managefiles/home.html', {"form": form})


# Show all files
@login_required
def dashboard(request):
    # Gets all the user files
    user_files = UserFile.objects.all()
    all_user_files = user_files.filter(trash=False)
    fav_user_files = user_files.filter(favourite=True)
    trash_user_files = user_files.filter(trash=True)
    
    if request.method =='POST':
        form = AddFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.owner = request.user
            new_file.save()
    else:
        form = AddFileForm()
    return render(request,
                  'managefiles/dashboard.html',
                  {'all_user_files': all_user_files,
                   'fav_user_files': fav_user_files,
                   'trash_user_files': trash_user_files,
                   'form': form})

# Delete File
@login_required
@require_POST
def file_delete(request, pk):
    plik = get_object_or_404(UserFile, pk=pk, owner=request.user)
    plik.delete()
    return redirect('managefiles:dashboard')

# Add to trash
@login_required
@require_POST
def add_to_trash(request, pk):
    plik = get_object_or_404(UserFile, pk=pk, owner=request.user)
    if plik.trash == True:
        plik.trash = False
    else:
        plik.trash = True
        plik.favourite = False
    plik.save()
    return redirect('managefiles:dashboard')

# Add to favourites
@login_required
@require_POST
def favourite(request, pk):
    plik = get_object_or_404(UserFile, pk=pk, owner=request.user)
    if plik.favourite == True:
        plik.favourite = False
    else:
        plik.favourite = True
        plik.trash = False
    plik.save()
    return redirect('managefiles:dashboard')
