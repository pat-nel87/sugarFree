from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from .forms import AuthenticationForm, UserCreateForm

def index(request):
    
    form = AuthenticationForm          
    return render(request, "index.html", {"form":form()})
    

def register(request):   
    
    form2 = UserCreateForm()
    
    if form2.is_valid():
      user = form2.save(commit=False) 
      user.save() 
      print(form2.errors)
    
    return render(request, "original.html", {"form2":form2})

def log_on(request):
    
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        return HttpResponse(f"{user}")
    else:
        return redirect('index')

def log_out(request):
    
    logout(request)
    
    return redirect('index')
        
    

