from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



from .forms import CreateUserForm

# Create your views here. 


def loginPage(request):
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


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Accounts has Created for {user}')
                return redirect("login")

    context: dict = {"form": form}
    return render(request, "accounts/register.html", context=context)

def logoutUser(request):
    logout(request) 
    return redirect('login')