from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm


def homepage(request):
    user = request.user
    if user.is_authenticated:
        profile = user.profile
        return redirect("my-profile")
    else:
        return redirect("login")


def profile(request):
    id = request.user.profile.id
    profile = Profile.objects.get(id=id)
    spiders = profile.spider_set.all()
    context = {"profile": profile, 'spiders': spiders}
    return render(request, 'users/my-profile.html', context)


def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect("my-profile")

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome back! We missed You ;)')
            return redirect('my-profile')
        else:
            messages.error(request, 'Userneme and/or password incorrect')
    context = {'page': page}
    return render(request, 'users/login_register.html', context)


def logoutUser(request):
    logout(request)
    messages.success(request, 'User logged out')
    return redirect("home")

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User created! Welcome to our family ;)")
            login(request, user)
            return redirect('my-profile')
        else:
            messages.error(request, "Something went wrong. Try again")
            
    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)
    

def updateProfile(request):
    id = request.user.profile.id
    profile = Profile.objects.get(id=id)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile is updated ;)")
        else:
            messages.error(request, "Sorry, error occured. Try again, please")
        return redirect("my-profile")
    context = {'form': form}
    return render(request, 'users/profile-form.html', context)