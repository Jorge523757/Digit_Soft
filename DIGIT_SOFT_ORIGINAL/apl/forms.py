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
<<<<<<< HEAD
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
        
    
=======
            'color': TextInput(attrs={'placeholder': 'Ingrese el color'}),
            'marca': TextInput(attrs={'placeholder': 'Ingrese la marca'}),
            'descripcion': Textarea(attrs={'placeholder': 'Ingrese una descripción', 'rows': 3, 'cols': 40}),
        }


class ProveedorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {
            'nit_proveedor': TextInput(attrs={'placeholder': 'Ingrese el NIT del proveedor'}),
            'nombre': TextInput(attrs={'placeholder': 'Ingrese el nombre'}),
            'cedula': TextInput(attrs={'placeholder': 'Ingrese la cédula'}),
            'direccion': TextInput(attrs={'placeholder': 'Ingrese la dirección'}),
            'telefono': TextInput(attrs={'placeholder': 'Ingrese el teléfono'}),
        }


class AdministradorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Administrador
        fields = '__all__'
        widgets = {
            'nombre': TextInput(attrs={'placeholder': 'Ingrese un nombre'}),
            'contrasena': PasswordInput(attrs={'placeholder': 'Ingrese la contraseña'}),
            'correo_electronico': TextInput(attrs={'placeholder': 'Ingrese el correo electrónico'}),
        }


class ProductoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre_producto'].widget.attrs['autofocus'] = True

    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre_producto': TextInput(attrs={'placeholder': 'Ingrese el nombre del producto'}),
            'modelo_producto': TextInput(attrs={'placeholder': 'Ingrese el modelo'}),
            'cantidad': NumberInput(attrs={'placeholder': 'Ingrese la cantidad'}),
            'valor_producto': TextInput(attrs={'placeholder': 'Ingrese el valor'}),
            'diseno': TextInput(attrs={'placeholder': 'Ingrese el diseño'}),
        }


class EquipoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['modelo'].widget.attrs['autofocus'] = True

    class Meta:
        model = Equipo
        fields = '__all__'
        widgets = {
            'modelo': TextInput(attrs={'placeholder': 'Ingrese el modelo'}),
            'clave': TextInput(attrs={'placeholder': 'Ingrese la clave'}),
        }


class TecnicoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre_completo'].widget.attrs['autofocus'] = True

    class Meta:
        model = Tecnico
        fields = '__all__'
        widgets = {
            'nombre_completo': TextInput(attrs={'placeholder': 'Ingrese el nombre completo'}),
            'n_documento': NumberInput(attrs={'placeholder': 'Ingrese el número de documento'}),
            'n_tel': NumberInput(attrs={'placeholder': 'Ingrese el teléfono'}),
            'correo': TextInput(attrs={'placeholder': 'Ingrese el correo electrónico'}),
            'direccion': TextInput(attrs={'placeholder': 'Ingrese la dirección'}),
            'especialidad': TextInput(attrs={'placeholder': 'Ingrese la especialidad'}),
            'tipo_tecnico': TextInput(attrs={'placeholder': 'Ingrese el tipo de técnico'}),
        }


class OrdenServicioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descripcion_orden'].widget.attrs['autofocus'] = True

    class Meta:
        model = OrdenServicio
        fields = '__all__'
        widgets = {
            'descripcion_orden': Textarea(attrs={'placeholder': 'Ingrese la descripción', 'rows': 3, 'cols': 40}),
        }


class ServicioTecnicoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['equipo'].widget.attrs['autofocus'] = True

    class Meta:
        model = ServicioTecnico
        fields = '__all__'
        widgets = {
            'equipo': TextInput(attrs={'placeholder': 'Ingrese el equipo'}),
            'descripcion_falla': Textarea(attrs={'placeholder': 'Describa la falla', 'rows': 3, 'cols': 40}),
            'fecha_ingreso': DateInput(attrs={'type': 'date'}),
            'fecha_entrega': DateInput(attrs={'type': 'date'}),
            'estado': TextInput(attrs={'placeholder': 'Ingrese el estado'}),
        }


class VentaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_venta'].widget.attrs['autofocus'] = True

    class Meta:
        model = Venta
        fields = '__all__'
        widgets = {
            'fecha_venta': DateInput(attrs={'type': 'date'}),
            'cantidad': NumberInput(attrs={'placeholder': 'Ingrese la cantidad'}),
            'total': NumberInput(attrs={'placeholder': 'Ingrese el total'}),
        }


class ComprasMercanciaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cantidad_compras'].widget.attrs['autofocus'] = True

    class Meta:
        model = ComprasMercancia
        fields = '__all__'
        widgets = {
            'cantidad_compras': NumberInput(attrs={'placeholder': 'Ingrese la cantidad'}),
            'fecha_compra': DateInput(attrs={'type': 'date'}),
            'precio_compra': TextInput(attrs={'placeholder': 'Ingrese el precio de compra'}),
        }


class FacturacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha'].widget.attrs['autofocus'] = True

    class Meta:
        model = Facturacion
        fields = '__all__'
        widgets = {
            'fecha': DateInput(attrs={'type': 'date'}),
            'descripcion_venta': Textarea(attrs={'placeholder': 'Ingrese una descripción', 'rows': 3, 'cols': 40}),
            'terminos_y_condiciones': Textarea(attrs={'placeholder': 'Ingrese los términos y condiciones', 'rows': 3, 'cols': 40}),
            'nit_digisoft': TextInput(attrs={'placeholder': 'Ingrese el NIT'}),
        }


class GarantiasForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['facturacion'].widget.attrs['autofocus'] = True

    class Meta:
        model = Garantias
        fields = '__all__'
>>>>>>> 8a7086eb60eed25f2e9073c9099ea59512ae7595
