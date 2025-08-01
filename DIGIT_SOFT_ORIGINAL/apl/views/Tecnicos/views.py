from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.http import JsonResponse

from apl.models import Tecnicos
from apl.forms import TecnicoForm

class TecnicoListView(ListView):
    model = Tecnicos
    template_name = 'tecnicos/listar_tecnicos.html'
    context_object_name = 'tecnicos'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {'nombre': 'DigitSoft'}
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Técnicos'
        context['crear_ruta_url'] = reverse_lazy('apl:tecnico_crear')
        context['entidad'] = 'Técnico'
        return context


class TecnicoCreateView(CreateView):
    model = Tecnicos
    form_class = TecnicoForm
    template_name = 'tecnicos/crear.html'
    success_url = reverse_lazy('apl:tecnico_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Técnico'
        return context


class TecnicoUpdateView(UpdateView):
    model = Tecnicos
    form_class = TecnicoForm
    template_name = 'tecnicos/crear.html'
    success_url = reverse_lazy('apl:tecnico_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Técnico'
        context['entidad'] = 'Técnico'
        context['listar_url'] = reverse_lazy('apl:tecnico_listar')
        return context


class TecnicoDeleteView(DeleteView):
    model = Tecnicos
    template_name = 'tecnicos/eliminar.html'
    success_url = reverse_lazy('apl:tecnico_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Técnico'
        context['entidad'] = 'Técnico'
        context['listar_url'] = reverse_lazy('apl:tecnico_listar')
        return context

