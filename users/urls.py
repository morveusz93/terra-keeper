from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="users"),
    path("<str:id>", views.profile, name="user-details"),
]
