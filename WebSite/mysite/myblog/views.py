from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .models import Post


def home(request):
    return render(request, 'home.html')


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'all_post_list': posts})


def single_post(request,post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'single_post.html', {'post': post})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'thankyou.html')
        else:
            return HttpResponse("Username or password incorrect")
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')



