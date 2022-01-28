from django.forms import ModelForm
from .models import Spider


class SpiderForm(ModelForm):
    class Meta:
        model = Spider
        fields = '__all__'

