from http.client import HTTPResponse

from django.contrib import messages
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect


# Create your views here.

def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully! You can now log in.')
            return redirect('login')  # Redirect to the login page after successful registration
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()

    return render(request, 'user/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('/')  # Redirect to a profile or homepage
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'user/login.html')

def logout_view(reqeust):
    logout(reqeust)
    return redirect('login')
