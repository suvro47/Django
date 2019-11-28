from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from .forms import RegistrationForm


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


#  no need to define login and logout views


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'all_user_list': users})


def single_user(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'single_user.html', {'user': user})

