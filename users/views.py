from django.shortcuts import render


def users(request):
    return render(request, 'users/users.html')

def newUser(request):
    return render(request, 'users/user-form')