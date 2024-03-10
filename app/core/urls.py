from django.urls import path
from core import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home , name='home'),
    path('profile/', views.profile, name='profile'),
    path('deploy/', views.deploy, name='deploy'),
]

