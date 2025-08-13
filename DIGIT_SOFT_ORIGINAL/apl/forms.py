from django.forms import *
from .models import *

from django import forms
from django.forms import ModelForm, TextInput, Textarea, PasswordInput, DateInput, NumberInput
from .models import (
    Cliente, Marca, Proveedor, Administrador, Producto, Equipo, Tecnico,
    OrdenServicio, ServicioTecnico, Venta, ComprasMercancia, Facturacion, Garantias
)

class ClienteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nombre': TextInput(attrs={'placeholder': 'Ingrese el nombre'}),
            'numero_documento': TextInput(attrs={'placeholder': 'Ingrese el número de documento'}),
            'numero_telefonico': TextInput(attrs={'placeholder': 'Ingrese el número telefónico'}),
            'correo_electronico': TextInput(attrs={'placeholder': 'Ingrese el correo electrónico'}),
            'direccion': TextInput(attrs={'placeholder': 'Ingrese la dirección'}),
        }


class MarcaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['color'].widget.attrs['autofocus'] = True

    class Meta:
        model = Marca
        fields = '__all__'
        widgets = {

            'color': TextInput(
                attrs={
                    'placeholder': 'Ingrese el color',
                    'class': 'form-control',
                }
            ),
            'marca': TextInput(
                attrs={
                    'placeholder': 'Ingrese la marca',
                    'class': 'form-control',
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'placeholder': 'Ingrese una descripción',
                    'rows': 3,
                    'cols': 40,
                }
            ),
        }
        
    

