from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User,auth


# Create your views here.

def home(request):
    blogs = Post.objects.all()
    context = {
        "blogs" : blogs
    }
    return render(request, 'home.html', context)


def postblog(request):
    blogs = Post.objects.all()
    context = {
        "blogs" : blogs
    }
    
    if request.method == "POST":
        name = request.POST['name']
        title = request.POST['title']
        body = request.POST['body']
        
        post = Post(name=name, title=title, body=body)
        post.save()
        messages.success(request, 'Successfully Created')
        
        return render(request, 'home.html', context)
    
    else:
        messages.error(request, 'Some Error Occoured')
        return render(request, 'home.html', context)
    
    
def register(request):
    blogs = Post.objects.all()
    context = {
        "blogs" : blogs
    }
    
    if request.method == 'POST':
        username = request.POST['username'] 
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return render(request, 'home.html', context)
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already in Use')
                return render(request, 'home.html', context)
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Successfully Registered')
                return render(request, 'home.html', context)
        else:
            messages.error(request, 'Passwords Do Not Match')  
            return render(request, 'home.html', context)
           
    return render(request, 'register.html')


def login(request):
    blogs = Post.objects.all()
    context = {
        "blogs" : blogs
    }
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return render(request, 'home.html', context)
        else:
            messages.error(request, 'Credentials Invalid')  
            return render(request, 'home.html', context)
        
    return render(request, 'home.html', context)


def logout(request):
    blogs = Post.objects.all()
    context = {
        "blogs" : blogs
    }
    
    auth.logout(request)
    return render(request, 'home.html', context)   
    
    
def post(request, post):
    post = Post.objects.get(id=post)
    return render(request, 'blog.html', {"post":post})
    
        
    
        
        
    
