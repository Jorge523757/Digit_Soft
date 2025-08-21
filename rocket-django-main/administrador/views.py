from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Administrador
from .forms import AdministradorForm

# ================= Administrador =================
class AdministradorList(ListView):
    model = Administrador
    template_name = "administrador/listar_administrador.html"
    context_object_name = "administradores"

class AdministradorCreate(CreateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = "administrador/crear.html"
    success_url = reverse_lazy("administrador_list")

class AdministradorUpdate(UpdateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = "administrador/crear.html"
    success_url = reverse_lazy("administrador_list")

class AdministradorDelete(DeleteView):
    model = Administrador
    template_name = "administrador/eliminar.html"
    success_url = reverse_lazy("administrador_list")



