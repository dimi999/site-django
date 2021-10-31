from django.shortcuts import render, redirect
from django.http import HttpResponse
from .templates.forms import CreateUser, ConnectUser
from django.contrib.auth import login, authenticate, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required       #@login_required(login_url = '/login')

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def loginPage(request):
    form = ConnectUser()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('/features')
        else:
            messages.info(request, "Username or password is incorrect")

    return render(request, 'login.html', {})

def registerPage(request):
    form = CreateUser()

    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = CreateUser()

    return render(request, 'register.html', {'form':form})

@login_required(login_url = '/login')
def features(request):
    return render(request, 'features.html', {})