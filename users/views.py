from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
from django.views.generic import CreateView, UpdateView

from .models import Profile
from .forms import CustomUserCreationForm


class CustomLoginView(LoginView):
    template_name = 'users/login_register.html'

    def get_redirect_url(self):
        return reverse('my-profile')

    def form_valid(self, form):
        messages.success(self.request, 'Welcome back! We missed You ;)')
        return super(CustomLoginView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Username or password is wrong. Try again')
        return super(CustomLoginView, self).form_invalid(form)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("home")

    def get_next_page(self):
        messages.success(self.request, 'User logged out.')
        return super(CustomLogoutView, self).get_next_page()


class RegisterView(CreateView):
    model = Profile
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('my-profile')
    template_name = 'users/login_register.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.username = self.object.username.lower()
        self.object.save()
        messages.success(self.request, "User created! Welcome to our family ;)")
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong :/ Try again.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'register'
        return context
    

class ProfileUpdateView(UpdateView):
    model = Profile
    success_url = reverse_lazy('my-profile')
    fields = ['username', 'email']

    def form_valid(self, form):
        messages.success(self.request, "User info updated!")
        return super(ProfileUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Something went wrong :/ Try again.")
        return super(ProfileUpdateView, self).form_invalid(form)


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'users/change_password.html'	
    success_url = reverse_lazy('my-profile')

    def form_valid(self, form):
        messages.success(self.request, 'Password changed')
        return super().form_valid(form)
        