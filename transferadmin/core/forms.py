from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Cliente, Transfer

class ClienteForm(forms.ModelForm):
    class Meta: 
        model= Cliente
        fields = ['nombre', 'rut', 'ciudad', 'comuna', 'direccion']
        labels ={
            'nombre': 'Nombre', 
            'rut': 'Rut', 
            'ciudad': 'Ciudad', 
            'comuna': 'Comuna', 
            'direccion': 'Direccion',
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut/pasaporte', 
                    'id': 'rut'
                }
            ), 
            'ciudad': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese ciudad', 
                    'id': 'ciudad'
                }
            ),
            'comuna': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese comuna', 
                    'id': 'comuna'
                }
            ),  
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese direccion', 
                    'id': 'direccion'
                }
            )
        }

class TransferForm(forms.ModelForm):
    class Meta: 
        model= Transfer
        fields = ['numero', 'asiento', 'hora', 'patente', 'nombreChofer']
        labels ={
            'numero': 'numero',
            'asiento': 'asiento',
            'hora': 'hora',
            'patente': 'Patente', 
            'nombreChofer': 'Nombre Chofer', 
        }
        widgets={
            'numero': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Numero de transfer', 
                    'id': 'numero'
                }
            ), 
            'asiento': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'asiento', 
                    'id': 'asiento'
                }
            ), 
            'hora': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'hora de salida', 
                    'id': 'hora'
                }
            ), 
            'patente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Patente', 
                    'id': 'patente'
                }
            ), 
            'nombreChofer': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Nombre Chofer', 
                    'id': 'nombreChofer'
                }
            )
        }