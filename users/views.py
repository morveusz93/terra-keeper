from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from .forms import CustomUserCreationForm


def index(request):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request, 'users/profiles.html', context)


def profile(request, id):
    profile = Profile.objects.get(id=id)
    context = {"profile": profile}
    return render(request, 'users/details.html', context)


def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect("profiles")

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Userneme and/or password incorrect')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome back! We missed You ;)')
            return redirect('profiles')
        else:
            messages.error(request, 'Userneme and/or password incorrect')
    context = {'page': page}
    return render(request, 'users/login_register.html', context)


def logoutUser(request):
    logout(request)
    messages.success(request, 'User logged out')
    return redirect("profiles")

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User created!")
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Something went wrong. Try again")
            


    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)
    