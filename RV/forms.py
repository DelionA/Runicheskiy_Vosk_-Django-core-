
from django import forms
from .models import RunicheskiyVosk, AnswersKeys
from django.core.exceptions import ValidationError
from .futark import Futark
from django.core import validators
from django.shortcuts import redirect

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

    def clean_runa_2(self):
        runa_2 = self.cleaned_data['runa_2']
        list_ = [i for i in self.cleaned_data.values()]

        if list_.count(runa_2) > 1:

            raise ValidationError('Вторая Руна должна быть уникальна !')
        return runa_2

    def clean_runa_3(self):
        runa_3 = self.cleaned_data['runa_3']
        list_ = [i for i in self.cleaned_data.values()]

        if list_.count(runa_3) > 1:

            raise ValidationError('Третья Руна должна быть уникальна !')
        return runa_3

    def clean_runa_4(self):
        runa_4 = self.cleaned_data['runa_4']
        list_ = [i for i in self.cleaned_data.values()]

        if list_.count(runa_4) > 1:

            raise ValidationError('Четвертая Руна должна быть уникальна !')
        return runa_4

    def clean_runa_5(self):
        runa_5 = self.cleaned_data['runa_5']
        list_ = [i for i in self.cleaned_data.values()]

        if list_.count(runa_5) > 1:

            raise ValidationError('Пятая Руна должна быть уникальна !')
        return runa_5

    def clean_runa_6(self):
        runa_6 = self.cleaned_data['runa_6']
        list_ = [i for i in self.cleaned_data.values()]

        if list_.count(runa_6) > 1:

            raise ValidationError('Шестая Руна должна быть уникальна !')
        return runa_6

    def clean_runa_7(self):
        runa_7 = self.cleaned_data['runa_7']
        list_ = [i for i in self.cleaned_data.values()]

        if list_.count(runa_7) > 1:

            raise ValidationError('Седьмая Руна должна быть уникальна !')
        return runa_7
    # def clean(self):
    #     print(dir(self.non_field_errors))
    #     list_ = [i for i in self.cleaned_data]
    #     for i in self.cleaned_data:
    #         if list_.count(i) > 1:
    #             raise ValidationError('Slug may not be "Create"')
    #     return super().clean()






class RunaFormResult(forms.ModelForm):
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
            'runa_7': forms.Select()
        }

class AnswersKeysForm(forms.ModelForm):
    class Meta:
        model = AnswersKeys
        fields = [

                'runa_1runa_7', 'runa_1runa_6', 'runa_1runa_5', 'runa_1runa_4',
                'runa_1runa_3', 'runa_1runa_2',
                'runa_2runa_7', 'runa_2runa_6', 'runa_2runa_5', 'runa_2runa_4',
                'runa_2runa_3',
                'runa_3runa_7', 'runa_3runa_6', 'runa_3runa_5', 'runa_3runa_4',
                'runa_4runa_7', 'runa_4runa_6', 'runa_4runa_5',
                'runa_5runa_7', 'runa_5runa_6',
                'runa_6runa_7',
                'runa_7runa_1', 'runa_6runa_1', 'runa_5runa_1', 'runa_4runa_1',
                'runa_3runa_1', 'runa_2runa_1',
                'runa_7runa_2', 'runa_6runa_2', 'runa_5runa_2', 'runa_4runa_2',
                'runa_3runa_2',
                'runa_7runa_3', 'runa_6runa_3', 'runa_5runa_3', 'runa_4runa_3',
                'runa_7runa_4', 'runa_6runa_4', 'runa_5runa_4',
                'runa_7runa_5', 'runa_6runa_5',
                'runa_7runa_6', 'rv_answers_keys'
        ]
        widget = {
            'runa_1runa_7': forms.CharField(max_length=20),
            'runa_1runa_6': forms.CharField(max_length=20),
            'runa_1runa_5': forms.CharField(max_length=20),
            'runa_1runa_4': forms.CharField(max_length=20),
            'runa_1runa_3': forms.CharField(max_length=20),
            'runa_1runa_2': forms.CharField(max_length=20),
            'runa_2runa_7': forms.CharField(max_length=20),
            'runa_2runa_6': forms.CharField(max_length=20),
            'runa_2runa_5': forms.CharField(max_length=20),
            'runa_2runa_4': forms.CharField(max_length=20),
            'runa_2runa_3': forms.CharField(max_length=20),
            'runa_3runa_7': forms.CharField(max_length=20),
            'runa_3runa_6': forms.CharField(max_length=20),
            'runa_3runa_5': forms.CharField(max_length=20),
            'runa_3runa_4': forms.CharField(max_length=20),
            'runa_4runa_7': forms.CharField(max_length=20),
            'runa_4runa_6': forms.CharField(max_length=20),
            'runa_4runa_5': forms.CharField(max_length=20),
            'runa_5runa_7': forms.CharField(max_length=20),
            'runa_5runa_6': forms.CharField(max_length=20),
            'runa_6runa_7': forms.CharField(max_length=20),
            'runa_7runa_1': forms.CharField(max_length=20),
            'runa_6runa_1': forms.CharField(max_length=20),
            'runa_5runa_1': forms.CharField(max_length=20),
            'runa_4runa_1': forms.CharField(max_length=20),
            'runa_3runa_1': forms.CharField(max_length=20),
            'runa_2runa_1': forms.CharField(max_length=20),
            'runa_7runa_2': forms.CharField(max_length=20),
            'runa_6runa_2': forms.CharField(max_length=20),
            'runa_5runa_2': forms.CharField(max_length=20),
            'runa_4runa_2': forms.CharField(max_length=20),
            'runa_3runa_2': forms.CharField(max_length=20),
            'runa_7runa_3': forms.CharField(max_length=20),
            'runa_6runa_3': forms.CharField(max_length=20),
            'runa_5runa_3': forms.CharField(max_length=20),
            'runa_4runa_3': forms.CharField(max_length=20),
            'runa_7runa_4': forms.CharField(max_length=20),
            'runa_6runa_4': forms.CharField(max_length=20),
            'runa_5runa_4': forms.CharField(max_length=20),
            'runa_7runa_5': forms.CharField(max_length=20),
            'runa_6runa_5': forms.CharField(max_length=20),
            'runa_7runa_6': forms.CharField(max_length=20),
            'rv_answers_keys': forms.CharField(max_length=20)

        }
