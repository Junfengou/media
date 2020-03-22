from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorator import unauthenticated_user, allowed_users
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

"""
from .forms import ImageCreateForm
"""


# Create your views here.

def welcome(request):
    return render(request, 'blog/welcome.html')


@login_required(login_url='blog-login')
# @allowed_users(allowed_roles=['admin'])
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'


@login_required(login_url='blog-login')
def recent(request):
    return render(request, 'blog/recent.html')


@login_required(login_url='blog-login')
def helpme(request):
    return render(request, 'blog/help.html')


# User now have the power to update their profile
# The u_form updates personal info
# p_form updates the image
@login_required(login_url='blog-login')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account info was successfully updated')
            return redirect('blog-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,

    }
    return render(request, 'blog/profile.html', context)


@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('blog-home')
                else:
                    messages.info(request, 'Disabled account')
                    return render(request, 'blog/login.html', {'form': form})
            else:
                messages.info(request, 'Invalid Login info')
                return render(request, 'blog/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('blog-login')


@unauthenticated_user
def user_register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('blog-login')
    return render(request, 'blog/register.html', {'form': form})


"""
@login_required(login_url='blog-login')
def image_created(request):
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)

    return render(request,
                  'blog/created.html',
                  {'section': 'images',
                   'form': form})
"""
