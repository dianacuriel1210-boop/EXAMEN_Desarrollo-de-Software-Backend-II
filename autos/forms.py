
from django import forms
from .models import Auto


class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['marca', 'modelo', 'año', 'precio']

        widgets = {
            'marca': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Toyota'
            }),
            'modelo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. Corolla'
            }),
            'año': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. 2024'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej. 250000.00',
                'step': '0.01'
            }),
        }
