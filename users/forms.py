from dataclasses import field
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.help_text = None


        self.fields['username'].widget.attrs.update({'placeholder': 'username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'confirm password'})
