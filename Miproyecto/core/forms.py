# core/forms.py
from django import forms
from .models import SolicitudAdopcion

class SolicitudAdopcionForm(forms.ModelForm):
    class Meta:
        model = SolicitudAdopcion
        fields = [
            'nombre',
            'edad',
            'metros_patio',
            'cupos_al_momento',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'metros_patio': forms.NumberInput(attrs={'class': 'form-control'}),
            'cupos_al_momento': forms.NumberInput(attrs={'class': 'form-control'}),
        }