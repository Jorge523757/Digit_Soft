from django import forms
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from apl.views.producto.views import *
from apl.models import Producto
from apl.forms import *
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
#from django.contrib.auth.decorators import login_required
from apl.models import *

# aqui estan las vistas de productos

class productoListview(ListView):
    model = Producto
    template_name = 'producto/listar_producto.html'
    context_object_name = 'producto'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'sofia'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Producto'
        context['crear_ruta_url'] = reverse_lazy('apl:producto_crear')
        context['entidad'] = 'producto'
        context['producto'] = Producto.objects.all()
        return context
    
class productoCreateView(CreateView):
    model = Producto
    form_class = productoform
    template_name = 'producto/crear.html'
    success_url = reverse_lazy('apl:producto_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear producto'
        return context

class productoUpdateView(UpdateView):
    model = Producto
    form_class = productoform
    template_name = 'producto/crear.html'
    success_url = reverse_lazy('apl:producto_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar producto'
        context['entidad'] = 'producto'
        context['listar_url'] = reverse_lazy('apl:producto_listar')
        return context

class productoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto/eliminar.html'
    success_url = reverse_lazy('apl:producto_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar producto'
        context['entidad'] = 'producto'
        context['listar_url'] = reverse_lazy('apl:producto_eliminar')
        return context
    