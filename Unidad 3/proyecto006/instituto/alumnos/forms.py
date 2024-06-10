from django import forms
from django.forms import ModelForm

from .models import Usuario


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields= "__all__"
        labels={
            'apellido1' : 'Apellido Paterno',
            'apellido2' : 'Apellido Materno'
        }
        widgets = {
            'email' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su correo'
            }),
            'nombre' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su nombre'
            }),'apellido1' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su apellido paterno'
            }),'apellido2' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su apellido materno'
            }),
        }