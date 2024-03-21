from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .forms import LoginForm , SignupForm , ProfileForm

def home(request):
    return render(request , "main/home.html")
def profile(request):
    return render(request , "main/profile.html")
def deploy(request):
    return render(request , "main/deploy.html")
# def login(request):
#     return render(request , "main/login.html")
# def register(request):
#     return render(request , "main/register.html")


def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'main/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('profile')

        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'main/home.html')

def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('')


def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = SignupForm()
    return render(request, 'main/register.html', {'form': form})


def edit_profile(request):
    user = request.user
    if user.is_authenticated:
        return redirect("home")
    profile = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'main/edit_profile.html', {'form': form})


def view_profile(request):
    return render(request, 'profile.html')