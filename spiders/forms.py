from django import forms
from .models import Molt, Spider


class SpiderForm(forms.ModelForm):
    class Meta:
        model = Spider
        fields = ['genus', 'species', 'name', 'sex', 'size', 'joined', "notes" ]
        widgets = {
          'genus': forms.TextInput(attrs={'placeholder': 'Genus'}),
          'species': forms.TextInput(attrs={'placeholder': 'Species'}),
          'name': forms.TextInput(attrs={'placeholder': 'Name'}),
          'size': forms.TextInput(attrs={'placeholder': 'Size in cm'}),
          'joined': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Date of join'}),
          'notes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Notes'}),
        }

    def __init__(self, *args, **kwargs):
        super(SpiderForm, self).__init__(*args, **kwargs)

        self.fields['sex'].empty_label = None
        if self.fields['sex'] and isinstance(self.fields['sex'] , forms.TypedChoiceField):
                self.fields['sex'].choices = self.fields['sex'].choices[1:]


class MoltForm(forms.ModelForm):
    class Meta:
        model = Molt
        fields = ['number', 'date']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'date'}),
            'number': forms.TextInput(attrs={'placeholder': 'Molt number'}),
        }
