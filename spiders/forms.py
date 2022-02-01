from django.forms import ModelForm, DateInput, TypedChoiceField
from .models import Molt, Spider


class SpiderForm(ModelForm):
    class Meta:
        model = Spider
        fields = ['genus', 'species', 'name', 'sex', 'size', 'joined' ]
        widgets = {
            'genus': DateInput(attrs={'placeholder': 'genus'}),
            'species': DateInput(attrs={'placeholder': 'species'}),
            'name': DateInput(attrs={'placeholder': 'name'}),
            'size': DateInput(attrs={'placeholder': 'size in cm'}),
            'joined': DateInput(attrs={'type': 'date', 'placeholder': 'joined'}),
        }

    def __init__(self, *args, **kwargs):
        super(SpiderForm, self).__init__(*args, **kwargs)

        self.fields['sex'].empty_label = None
        if self.fields['sex'] and isinstance(self.fields['sex'] , TypedChoiceField):
                self.fields['sex'].choices = self.fields['sex'].choices[1:]


class MoltForm(ModelForm):
    class Meta:
        model = Molt
        fields = ['number', 'date']

        widgets = {
            'date': DateInput(attrs={'type': 'date', 'placeholder': 'date'}),
            'molt': DateInput(attrs={'placeholder': 'molt'}),
        }