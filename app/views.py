from django.shortcuts import render, redirect
from .models import Post
from django.template import RequestContext
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User

def home(request):
    if(request.user.is_authenticated == False):
        return redirect("/login")
    context = {
        'posts': Post.objects.all(),
    }
    return render(request,'index.html', context)

def blog(request, id):
    if(request.user.is_authenticated == False):
        return redirect("/login")
    if(Post.objects.filter(id=id).exists() == False):
        return redirect("/")

    
    context = {
        'post': Post.objects.filter(id=id),
    }
    return render(request,'Blog.html', context)

def loginV(request):
    if(request.method == "POST"):
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if(user is not None):
            login(request, user)
            return redirect("/")
    
    if(request.user.is_authenticated == True):
        return redirect("/")
    


    return render(request,'login.html')


def logoutV(request):
    if(request.user.is_authenticated == True):
        logout(request)

    
    return redirect('/')


def registerV(request):
    if(request.user.is_authenticated == True):
        return redirect('/')
    if(request.method == "POST"):
        if(User.objects.filter(username=request.POST['username']).exists() == False):
            if(User.objects.filter(username=request.POST['email']).exists() == False):
                user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
                user.save()
                login(request, user)
                return redirect("/")
    
    return render(request, 'Register.html')

