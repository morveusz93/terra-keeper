from multiprocessing.spawn import import_main_path
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile


def index(request):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request, 'users/profiles.html', context)


def profile(request, id):
    profile = Profile.objects.get(id=id)
    context = {"profile": profile}
    return render(request, 'users/details.html', context)


def loginUser(request):
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
            print("logged in")
            return redirect('profiles')
        else:
            messages.error(request, 'Userneme and/or password incorrect')

    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.error(request, 'User logged out')
    return redirect("profiles")
