from django.forms import ModelForm, DateInput, TypedChoiceField
from .models import Spider


class SpiderForm(ModelForm):
    class Meta:
        model = Spider
        fields = ['genus', 'species', 'name', 'sex', 'size', 'joined' ]
        widgets = {
            'joined': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(SpiderForm, self).__init__(*args, **kwargs)

        self.fields['genus'].widget.attrs.update({'placeholder': 'genus'})
        self.fields['species'].widget.attrs.update({'placeholder': 'species'})
        self.fields['name'].widget.attrs.update({'placeholder': 'name'})
        self.fields['size'].widget.attrs.update({'placeholder': 'size'})
        self.fields['joined'].widget.attrs.update({'placeholder': 'joined'})
        self.fields['sex'].empty_label = None
        if self.fields['sex'] and isinstance(self.fields['sex'] , TypedChoiceField):
                self.fields['sex'].choices = self.fields['sex'].choices[1:]