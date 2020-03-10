from django.urls import path
from . import views
urlpatterns = [
    path('', views.login, name='blog-login'),
    path('home/', views.home, name='blog-home'),
    path('recent/', views.recent, name='blog-recent'),
    path('help/', views.help, name='blog-help'),
    path('profile/', views.profile, name='blog-profile'),
]