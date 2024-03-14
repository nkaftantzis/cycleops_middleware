from django.urls import path
from core import views

# app_name = 'user'

urlpatterns = [
    path('', views.sign_in, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home , name='home'),
    path('profile/', views.profile, name='profile'),
    path('deploy/', views.deploy, name='deploy'),
    path('logout/', views.sign_out, name='logout'),
]
