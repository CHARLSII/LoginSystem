from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages

from django.contrib.auth import get_user_model

User = get_user_model()


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
    if request.method == 'POST':
        full_name = request.POST.get("full_name")
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone_number = request.POST.get("phone_number")
        birthdate = request.POST.get("birthdate")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is taken")
            return redirect('register')
        
        user = User.objects.create_user(
            username = username,
            password = password,
            email = email,
        )
        
        if full_name:
            parts = full_name.split(" ", 1)
            user.first_name = parts[0]
            if len(parts) > 1:
                user.last_name = parts[1]
        user.phone_number = phone_number
        user.birthdate = birthdate
        user.save()
            
        auth_login(request, user)
        return redirect("index")
    
    
    return render(request, 'register.html')


def forgot(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        
        if User.objects.filter(email=email).exists():
            messages.success(request, f"Password Reset Instruction sent to {email}")
        else:
            messages.error(request, f"No account found with an Email:{email}")
    return render(request, 'forgot.html')


