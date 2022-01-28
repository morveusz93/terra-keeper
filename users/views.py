from django.shortcuts import render
from .models import Profile


def index(request):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request, 'users/profiles.html', context)


def profile(request, id):
    profile = Profile.objects.get(id=id)
    context = {"profile": profile}
    return render(request, 'users/details.html', context)


def newUser(request):
    return render(request, 'users/user-form')
