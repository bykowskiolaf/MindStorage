from django.shortcuts import render
from .forms import SignupForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        user_form = SignupForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
                          'registration/signup_done.html',
                          {'new_user': new_user})
    else:
        user_form = SignupForm()
    return render(request,
                  'registration/signup.html',
                  {'user_form': user_form})