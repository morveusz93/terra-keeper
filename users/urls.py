from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.registerUser, name="register"),

    path("myprofile", views.profile, name="my-profile"),
    path("myprofile/edit", views.updateProfile, name="profile-update"),
]
