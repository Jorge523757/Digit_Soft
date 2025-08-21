from django import forms
from .models import *

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = '__all__'

