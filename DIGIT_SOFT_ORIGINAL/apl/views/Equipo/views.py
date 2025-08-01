from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apl.models import Equipo
from apl.forms import EquipoForm

class EquipoListView(ListView):
    model = Equipo
    template_name = 'Equipos/listar_equipos.html'
    context_object_name = 'equipos'

class EquipoCreateView(CreateView):
    model = Equipo
    form_class = EquipoForm
    template_name = 'Equipos/crear.html'
    success_url = reverse_lazy('apl:listar_equipos')

class EquipoUpdateView(UpdateView):
    model = Equipo
    form_class = EquipoForm
    template_name = 'Equipos/crear.html'
    success_url = reverse_lazy('apl:listar_equipos')

class EquipoDeleteView(DeleteView):
    model = Equipo
    template_name = 'Equipos/eliminar.html'
    success_url = reverse_lazy('apl:listar_equipos')

