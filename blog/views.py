from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def welcome(request):
    return render(request, 'blog/welcome.html')


def home(request):
    return render(request, 'blog/home.html')


def recent(request):
    return render(request, 'blog/recent.html')


def helpme(request):
    return render(request, 'blog/help.html')


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
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})


def user_register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'blog/register.html', {'form': form})
