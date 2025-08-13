from django import forms
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from apl.views.marca.views import *
#from apl.models import Categoria
from apl.forms import *
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
#from django.contrib.auth.decorators import login_required
from apl.models import *

# aqui estan las vistas de marca

class marcaListview(ListView):
    model = Marca
    template_name = 'marca/listar_marca.html'
    context_object_name = 'marcas'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'sofia'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de marcas'
        context['crear_ruta_url'] = reverse_lazy('apl:marca_listar')
        context['entidad'] = 'marcas'
        context['marcas'] = Marca.objects.all()
        return context
    
class marcaCreateView(CreateView):
    model = Marca
    form_class = marcaform
    template_name = 'marca/crear.html'
    success_url = reverse_lazy('apl:marca_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear marcas'
        return context

class marcaUpdateView(UpdateView):
    model = Marca
    form_class = marcaform
    template_name = 'marca/crear.html'
    success_url = reverse_lazy('apl:marca_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar marcas'
        context['entidad'] = 'marcas'
        context['listar_url'] = reverse_lazy('apl:marca_editar')
        return context

class marcaDeleteView(DeleteView):
    model = Marca
    template_name = 'marca/eliminar.html'
    success_url = reverse_lazy('apl:marca_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar marcas'
        context['entidad'] = 'marcas'
        context['listar_url'] = reverse_lazy('apl:marca_eliminar')
        return context