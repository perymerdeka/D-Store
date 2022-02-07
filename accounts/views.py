from typing import Callable
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

from accounts.decorators import unauthenticated_user
from dashboard.decorators import allowed_users



from .forms import CreateUserForm

# Create your views here. 

@unauthenticated_user
def loginPage(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'User or password is incorrect')
            return redirect('login')
    
    
    context: dict = {}
    return render(request, "accounts/login.html", context=context)

@unauthenticated_user
def registerPage(request: HttpRequest):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request, f'Accounts has Created for {username}')
            return redirect("login")

    context: dict = {"form": form}
    return render(request, "accounts/register.html", context=context)


def logoutUser(request: HttpRequest):
    logout(request) 
    return redirect('login')
