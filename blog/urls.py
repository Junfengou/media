from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('', views.welcome, name='blog-welcome'),
    path('login/', views.user_login, name='blog-login'),
    path('logout/', views.user_logout, name='blog-logout'),
    path('register/', views.user_register, name='blog-register'),
    path('recent/', views.recent, name='blog-recent'),
    path('help/', views.helpme, name='blog-help'),
    path('profile/', views.profile, name='blog-profile'),
    path('home/', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Path below are for reset passwords
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='blog/resetpassword.html'),
         name='reset_password'),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='blog/resetpasswordsent.html'),
         name='password_reset_done'),

    path('reset_password/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='blog/resetpasswordform.html'),
         name='password_reset_confirm'),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='blog/resetpasswordcomplete.html'),
         name='password_reset_complete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
