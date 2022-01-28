from django.forms import ModelForm
from .models import Profile

class Profile(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
