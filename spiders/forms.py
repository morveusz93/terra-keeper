from django.forms import ModelForm, DateInput, DateField
from .models import Spider


class SpiderForm(ModelForm):
    class Meta:
        model = Spider
        fields = ['genus', 'species', 'name', 'molt', 'size', 'joined' ]
        widgets = {
            'joined': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(SpiderForm, self).__init__(*args, **kwargs)


        self.fields['genus'].widget.attrs.update({'class': 'fadeIn first', 'placeholder': 'genus'})
        self.fields['species'].widget.attrs.update({'class': 'fadeIn second', 'placeholder': 'species'})
        self.fields['name'].widget.attrs.update({'class': 'fadeIn third', 'placeholder': 'name'})
        self.fields['molt'].widget.attrs.update({'class': 'fadeIn fourth', 'placeholder': 'molt'})
        self.fields['size'].widget.attrs.update({'class': 'fadeIn fifth', 'placeholder': 'size'})
        self.fields['joined'].widget.attrs.update({'class': 'fadeIn sixth', 'placeholder': 'joined'})