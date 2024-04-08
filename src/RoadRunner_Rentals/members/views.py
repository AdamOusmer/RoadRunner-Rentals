from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterUserForm
from django.contrib import messages

# Create your views here.


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate User
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect back to the previous page or 'home' if no previous page
            redirect_to = request.session.get('redirect_to', 'home')
            # Clear redirect_to from session
            if 'redirect_to' in request.session:
                del request.session['redirect_to']
            return redirect(redirect_to)
        else:
            messages.error(request, 'There was an error logging in. Please try again.')
            return redirect('login')

    else:
        # Store the referring URL in session
        if 'HTTP_REFERER' in request.META:
            request.session['redirect_to'] = request.META['HTTP_REFERER']
        return render(request, 'authentification/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    form = RegisterUserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # Log the user in
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.success(request, f"{msg}: {form.error_messages[msg]}")
            return render(request, 'authentification/register.html', {'form': form})
    return render(request, 'authentification/register.html', {'form': form})

def profile(request):
    return render(request, 'profile/profile.html')
