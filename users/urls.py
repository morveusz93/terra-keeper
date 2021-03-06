from django.urls import path
from .views import CustomLoginView, CustomLogoutView, RegisterView, ProfileUpdateView, CustomPasswordChangeView


urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', CustomLogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('<str:pk>/edit', ProfileUpdateView.as_view(), name='profile-update' ),
    path('password', CustomPasswordChangeView.as_view(), name='change-password'),
]
