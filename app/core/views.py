from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request , "main/home.html")
def profile(request):
    return render(request , "main/profile.html")
def deploy(request):
    return render(request , "main/deploy.html")
def login(request):
    return render(request , "main/login.html")
def register(request):
    return render(request , "main/register.html")
