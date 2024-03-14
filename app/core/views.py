from django.shortcuts import render, redirect
from django.http import HttpResponse

# from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from .forms import LoginForm

def home(request):
    return render(request , "main/home.html")
def profile(request):
    return render(request , "main/profile.html")
def deploy(request):
    return render(request , "main/deploy.html")
# def login(request):
#     return render(request , "main/login.html")
def register(request):
    return render(request , "main/register.html")



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
        return render(request,'home.html')

def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('')
# class MyLoginView(LoginView):
#     redirect_authenticated_user = False

#     def get_success_url(self):
#         return reverse_lazy('profile')

#     def form_invalid(self, form):
#         messages.error(self.request,'Invalid username or password')
#         return self.render_to_response(self.get_context_data(form=form))