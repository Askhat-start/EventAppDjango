from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from main.models import *
# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = CustomUserCreationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return redirect('/')
    register_form = CustomUserCreationForm
    return render(request, 'user_auth/register.html', context={'register_form': register_form})


def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

    login_form = AuthenticationForm()
    return render(request=request, template_name='user_auth/login.html', context={'login_form': login_form})


def user_logout(request):
    logout(request)
