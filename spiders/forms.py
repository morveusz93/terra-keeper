from django.forms import ModelForm, DateInput, TypedChoiceField
from .models import Molt, Spider


class SpiderForm(ModelForm):
    class Meta:
        model = Spider
        fields = ['genus', 'species', 'name', 'sex', 'size', 'joined' ]
        widgets = {
            'joined': DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(SpiderForm, self).__init__(*args, **kwargs)

        self.fields['genus'].widget.attrs.update({'placeholder': 'genus'})
        self.fields['species'].widget.attrs.update({'placeholder': 'species'})
        self.fields['name'].widget.attrs.update({'placeholder': 'name'})
        self.fields['size'].widget.attrs.update({'placeholder': 'size in cm'})
        self.fields['joined'].widget.attrs.update({'placeholder': 'joined'})
        self.fields['sex'].empty_label = None
        if self.fields['sex'] and isinstance(self.fields['sex'] , TypedChoiceField):
                self.fields['sex'].choices = self.fields['sex'].choices[1:]


class MoltForm(ModelForm):
    class Meta:
        model = Molt
        fields = ['number', 'date']

        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }


    def __init__(self, *args, **kwargs):
        super(MoltForm, self).__init__(*args, **kwargs)

        self.fields['number'].widget.attrs.update({'placeholder': 'molt'})
        self.fields['date'].widget.attrs.update({'placeholder': 'date'})