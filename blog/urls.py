from django.urls import path
from . import views
urlpatterns = [
    path('', views.user_login, name='blog-login'),
    #path('', auth_views.LoginView.as_view, name='login'),
    #path('logout', auth_views.LogoutView.as_view, name='logout'),


    path('home/', views.home, name='blog-home'),
    path('recent/', views.recent, name='blog-recent'),
    path('help/', views.helpme, name='blog-help'),
    path('profile/', views.profile, name='blog-profile'),
]