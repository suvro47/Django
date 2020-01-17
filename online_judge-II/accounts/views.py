from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    """
        url: http://127.0.0.1:8000/accounts/login/
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    """
        url: http://127.0.0.1:8000/accounts/register/
    """
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not Matching....')
            return redirect('register')
    else:
        return render(request, 'register.html')


def user_logout(request):
    auth.logout(request)
    return redirect('home')


