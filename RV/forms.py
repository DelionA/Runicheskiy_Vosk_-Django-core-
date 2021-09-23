
from django import forms
from .models import RunicheskiyVosk

class RunaForm(forms.ModelForm):
    class Meta:
        model = RunicheskiyVosk
        fields = [
            'runa_1', 'runa_2', 'runa_3',
            'runa_4', 'runa_5', 'runa_6',
            'runa_7'
        ]
        widgets = {
            'runa_1': forms.Select(),
            'runa_2': forms.Select(),
            'runa_3': forms.Select(),
            'runa_4': forms.Select(),
            'runa_5': forms.Select(),
            'runa_6': forms.Select(),
            'runa_7': forms.Select(),
        }
