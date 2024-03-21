from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User , UserManager , Profile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']
