from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apl.models import ServicioTecnico
from apl.forms import ServicioTecnicoForm

class ServicioTecnicoListView(ListView):
    model = ServicioTecnico
    template_name = 'ServicioTecnico/listar_serviciotecnico.html'
    context_object_name = 'servicio_list'

class ServicioTecnicoCreateView(CreateView):
    model = ServicioTecnico
    form_class = ServicioTecnicoForm
    template_name = 'ServicioTecnico/crear.html'
    success_url = reverse_lazy('apl:servicio_listar')

class ServicioTecnicoUpdateView(UpdateView):
    model = ServicioTecnico
    form_class = ServicioTecnicoForm
    template_name = 'ServicioTecnico/crear.html'
    success_url = reverse_lazy('apl:servicio_listar')

class ServicioTecnicoDeleteView(DeleteView):
    model = ServicioTecnico
    template_name = 'ServicioTecnico/eliminar.html'
    success_url = reverse_lazy('apl:servicio_listar')
