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

    # Path below are for reset passwords
    path('resetpassword/',
         auth_views.PasswordResetView.as_view(template_name='blog/resetpassword.html'),
         name='reset_password'),

    path('resetpasswordsent/',
         auth_views.PasswordResetDoneView.as_view(template_name='blog/resetpasswordsent.html'),
         name='password_reset_done'),

    path('resetpassword/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='blog/resetpasswordform.html'),
         name='password_reset_confirm'),

    path('resetpasswordcomplete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='blog/resetpasswordcomplete.html'),
         name='password_reset_complete'),
]
