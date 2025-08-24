from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth import logout
from .models import Users


# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Welcome")
            return redirect('index')
        else:
            messages.error(request, 'Invalid Username or Password')
            
    return render(request, 'login.html')
    

def logout_view(request):
    logout(request)
    return redirect('login')
    


def register(request):
    return render(request, 'register.html')


def forgot(request):
    return render(request, 'forgot.html')


