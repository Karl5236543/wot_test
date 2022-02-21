from django import forms
from django.core.checks import messages
from django.forms import fields, widgets
from django.forms.models import ModelChoiceField
from .models import Tank, TankProperties, Player
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.forms import modelform_factory

# class TankForm(forms.ModelForm):
#     class Meta:
#         model = Tank
#         fields = '__all__'
#
#     def clean_name(self):
#         errors = []
#         print("start form.clean_form()...")
#         name = self.cleaned_data['name']
#         print("stop form.clean_form()...")
#         return self.cleaned_data
#
#     def clean(self):
#         print("start form.clean()...")
#         print("end form.clean()...")
#
#     def save(self, *args, **kwargs):
#         print("start form.save()")
#         obj = super().save(*args, **kwargs)
#         print("stop form.save()")
#         return obj


# class TankForm(forms.Form):
#     name = forms.CharField(max_length=50, required=True)
#     lvl = forms.IntegerField(required=True)
#     premium = forms.BooleanField(required=False, widget=widgets.CheckboxInput)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.objects_errors = []

#     def clean_name(self):
#         errors = []
#         print("start form.clean_form()...")
#         name = self.cleaned_data['name']
#         print("stop form.clean_form()...")
#         return self.cleaned_data

#     def clean(self):
#         print("start form.clean()...")
#         for num in range(10):
#             tank = Tank(**self.cleaned_data)
#             try:
#                 tank.full_clean()
#             except ValidationError as e:
#                 self.objects_errors.append({'name': f'column {num}', 'error': e.message_dict})
#         if self.objects_errors:
#             raise ValidationError('Не верно указаны значения в таблице')
#         print("end form.clean()...")

#     def save(self, **kwargs):
#         print(self.cleaned_data)
#         return Tank(**self.cleaned_data).save(**kwargs)


class TankForm(forms.ModelForm):
    
    comment = forms.CharField(max_length=50, label='комментарий')

    class Meta:
        model = Tank
        fields = '__all__'
        help_texts = {
            'premium': 'ты хочешь заработать денег или нет?'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lvl'].initial = 1
        self.fields['name'].initial = 'новая имба'



class TankPropertiesForm(forms.ModelForm):
    tank = ModelChoiceField(
        queryset=Tank.objects.filter(properties=None),
        widget=widgets.RadioSelect(),
    )

    class Meta:
        model = TankProperties
        fields = '__all__'


class PlayerForm(forms.ModelForm):
    description = forms.CharField(max_length=255, required=False, empty_value='+380-98-851-26-68')
    wins_count = forms.CharField(max_length=10)
    tanks = forms.ModelMultipleChoiceField(queryset=Tank.objects.all())

    class Meta:
        Player,
        help_texts={
            'name': 'придумайте свой игровой ник'
        }