from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.welcome, name='blog-welcome'),
    path('login/', views.user_login, name='blog-login'),
    path('logout/', views.user_logout, name='blog-logout'),
    path('register/', views.user_register, name='blog-register'),
    path('home/', views.home, name='blog-home'),
    path('recent/', views.recent, name='blog-recent'),
    path('help/', views.helpme, name='blog-help'),
    path('profile/', views.profile, name='blog-profile'),
]