from django import forms
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from apl.views.garantias.views import *
from apl.models import Garantias
from apl.forms import *
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
#from django.contrib.auth.decorators import login_required
from apl.models import *

#aqui estan las vistas de garantia

class garantiasListview(ListView):
    model = Garantias
    template_name = 'garantia/listar_garantia.html'
    context_object_name = 'garantias'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'sofia'}
        return JsonResponse(nombre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Garantías'
        context['crear_ruta_url'] = reverse_lazy('apl:garantia_crear')
        context['entidad'] = 'garantías'
        context['garantias'] = Garantias.objects.all()
        return context
    
class garantiasCreateView(CreateView):
    model = Garantias
    form_class = garantiasform
    template_name = 'garantia/crear.html'
    success_url = reverse_lazy('apl:garantia_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear garantías'
        return context
    
class garantiasUpdateView(UpdateView):
    model = Garantias
    form_class = garantiasform
    template_name = 'garantia/crear.html'
    success_url = reverse_lazy('apl:garantia_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar garantías'
        context['entidad'] = 'garantías'
        context['listar_url'] = reverse_lazy('apl:garantia_editar')
        return context    
    
class garantiasDeleteView(DeleteView):
    model = Garantias
    template_name = 'garantia/eliminar.html'
    success_url = reverse_lazy('apl:garantia_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar garantías'
        context['entidad'] = 'garantías'
        context['listar_url'] = reverse_lazy('apl:garantia_eliminar')
        return context