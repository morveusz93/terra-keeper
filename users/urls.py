from django.urls import path
from . import views

urlpatterns = [
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),

    path('', views.index, name="profiles"),
    path("<str:id>", views.profile, name="user-details"),
]
