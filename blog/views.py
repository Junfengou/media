from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def welcome(request):
    return render(request, 'blog/welcome.html')


@login_required(login_url='blog-login')
def home(request):
    return render(request, 'blog/home.html')


@login_required(login_url='blog-login')
def recent(request):
    return render(request, 'blog/recent.html')


@login_required(login_url='blog-login')
def helpme(request):
    return render(request, 'blog/help.html')


@login_required(login_url='blog-login')
def profile(request):
    return render(request, 'blog/profile.html')


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
