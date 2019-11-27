from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def home(request):
    """
    url: http://127.0.0.1:8000
    """
    return render(request, 'home.html')
