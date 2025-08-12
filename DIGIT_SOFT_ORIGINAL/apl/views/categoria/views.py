from django import forms
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse_lazy
from apl.forms import *
from apl.models import *

# ===================== Vistas base =====================

def base_html(request):
    data = {
        'title': 'Base Template',
        'message': 'Welcome to the base template of the application.'
    }
    return render(request, 'categoria/content.html', data)

def plantilla_html(request):
    data = {
        'title': 'Plantilla HTML',
        'message': 'This is a sample HTML template.'
    }
    return render(request, 'categoria/plantilla.html', data)

# ===================== Mixin reutilizable =====================

class BaseListView(ListView):
    """Mixin para ListView con configuración común"""
    entidad = ''  # Atributo para definir la entidad
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return JsonResponse({'nombre': 'giovanny'})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['crear_ruta_url'] = reverse_lazy(f'apl:{self.entidad}_crear')
        context['entidad'] = self.entidad
        return context

class BaseCreateView(CreateView):
    """Mixin para CreateView con título dinámico"""
    entidad = '' # Atributo para definir la entidad
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = f'Crear {self.entidad.capitalize()}'
        return context

class BaseUpdateView(UpdateView):
    """Mixin para UpdateView con título y URLs"""
    entidad = '' # Atributo para definir la entidad
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = f'Editar {self.entidad.capitalize()}'
        context['entidad'] = self.entidad
        context['listar_url'] = reverse_lazy(f'apl:{self.entidad}_listar')
        return context

class BaseDeleteView(DeleteView):
    """Mixin para DeleteView con título y URLs"""
    entidad = '' # Atributo para definir la entidad
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = f'Eliminar {self.entidad.capitalize()}'
        context['entidad'] = self.entidad
        context['listar_url'] = reverse_lazy(f'apl:{self.entidad}_listar')
        return context

# ===================== Administrador =====================

class AdministradorListView(BaseListView):
    model = Administrador
    template_name = 'administrador/listar_administrador.html'
    context_object_name = 'administradores'
    entidad = 'administrador'

class AdministradorCreateView(BaseCreateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = 'administrador/crear.html'
    success_url = reverse_lazy('apl:administrador_listar')
    entidad = 'administrador'

class AdministradorUpdateView(BaseUpdateView):
    model = Administrador
    form_class = AdministradorForm
    template_name = 'administrador/crear.html'
    success_url = reverse_lazy('apl:administrador_listar')
    entidad = 'administrador'

class AdministradorDeleteView(BaseDeleteView):
    model = Administrador
    template_name = 'administrador/eliminar.html'
    success_url = reverse_lazy('apl:administrador_listar')
    entidad = 'administrador'

# ===================== Facturacion =====================

class FacturacionListView(BaseListView):
    model = Facturacion
    template_name = 'facturacion/listar_facturacion.html'
    context_object_name = 'facturaciones'
    entidad = 'facturacion'

class FacturacionCreateView(BaseCreateView):
    model = Facturacion
    form_class = FacturacionForm
    template_name = 'facturacion/crear.html'
    success_url = reverse_lazy('apl:facturacion_listar')
    entidad = 'facturacion'

class FacturacionUpdateView(BaseUpdateView):
    model = Facturacion
    form_class = FacturacionForm
    template_name = 'facturacion/crear.html'
    success_url = reverse_lazy('apl:facturacion_listar')
    entidad = 'facturacion'

class FacturacionDeleteView(BaseDeleteView):
    model = Facturacion
    template_name = 'facturacion/eliminar.html'
    success_url = reverse_lazy('apl:facturacion_listar')
    entidad = 'facturacion'

# ===================== Cliente =====================

class ClienteListView(BaseListView):
    model = Cliente
    template_name = 'cliente/listar_cliente.html'
    context_object_name = 'clientes'
    entidad = 'cliente'

class ClienteCreateView(BaseCreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/crear.html'
    success_url = reverse_lazy('apl:cliente_listar')
    entidad = 'cliente'

class ClienteUpdateView(BaseUpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/crear.html'
    success_url = reverse_lazy('apl:cliente_listar')
    entidad = 'cliente'

class ClienteDeleteView(BaseDeleteView):
    model = Cliente
    template_name = 'cliente/eliminar.html'
    success_url = reverse_lazy('apl:cliente_listar')
    entidad = 'cliente'

# ===================== Marca =====================

class MarcaListView(BaseListView):
    model = Marca
    template_name = 'Marca/listar_marca.html'
    context_object_name = 'marcas'
    entidad = 'marca'

class MarcaCreateView(BaseCreateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'Marca/crear.html'
    success_url = reverse_lazy('apl:marca_listar')
    entidad = 'marca'

class MarcaUpdateView(BaseUpdateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'Marca/crear.html'
    success_url = reverse_lazy('apl:marca_listar')
    entidad = 'marca'

class MarcaDeleteView(BaseDeleteView):
    model = Marca
    template_name = 'Marca/eliminar.html'
    success_url = reverse_lazy('apl:marca_listar')
    entidad = 'marca'

# ===================== Proveedor =====================

class ProveedorListView(BaseListView):
    model = Proveedor
    template_name = "Proveedor/listar_proveedor.html"
    context_object_name = "proveedores"
    entidad = "proveedor"

class ProveedorCreateView(BaseCreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = "Proveedor/crear.html"
    success_url = reverse_lazy("apl:proveedor_listar")
    entidad = "proveedor"

class ProveedorUpdateView(BaseUpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = "Proveedor/crear.html"
    success_url = reverse_lazy("apl:proveedor_listar")
    entidad = "proveedor"

class ProveedorDeleteView(BaseDeleteView):
    model = Proveedor
    template_name = "Proveedor/eliminar.html"
    success_url = reverse_lazy("apl:proveedor_listar")
    entidad = "proveedor"

# ===================== Producto =====================

class ProductoListView(BaseListView):
    model = Producto
    template_name = "Producto/listar_producto.html"
    context_object_name = "productos"
    entidad = "producto"

class ProductoCreateView(BaseCreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "Producto/crear.html"
    success_url = reverse_lazy("apl:producto_listar")
    entidad = "producto"

class ProductoUpdateView(BaseUpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "Producto/crear.html"
    success_url = reverse_lazy("apl:producto_listar")
    entidad = "producto"

class ProductoDeleteView(BaseDeleteView):
    model = Producto
    template_name = "Producto/eliminar.html"
    success_url = reverse_lazy("apl:producto_listar")
    entidad = "producto"

# ===================== Equipo =====================

class EquipoListView(BaseListView):
    model = Equipo
    template_name = "Equipo/listar_equipo.html"
    context_object_name = "equipos"
    entidad = "equipo"

class EquipoCreateView(BaseCreateView):
    model = Equipo
    form_class = EquipoForm
    template_name = "Equipo/crear.html"
    success_url = reverse_lazy("apl:equipo_listar")
    entidad = "equipo"

class EquipoUpdateView(BaseUpdateView):
    model = Equipo
    form_class = EquipoForm
    template_name = "Equipo/crear.html"
    success_url = reverse_lazy("apl:equipo_listar")
    entidad = "equipo"

class EquipoDeleteView(BaseDeleteView):
    model = Equipo
    template_name = "Equipo/eliminar.html"
    success_url = reverse_lazy("apl:equipo_listar")
    entidad = "equipo"

# ===================== Tecnico =====================

# ===================== Tecnico =====================

class TecnicoListView(BaseListView):
    model = Tecnico
    template_name = "Tecnicos/listar_tecnicos.html"
    context_object_name = "tecnicos"
    entidad = "tecnico"

class TecnicoCreateView(BaseCreateView):
    model = Tecnico
    form_class = TecnicoForm
    template_name = "Tecnicos/crear.html"
    success_url = reverse_lazy("apl:tecnico_listar")
    entidad = "tecnico"

class TecnicoUpdateView(BaseUpdateView):
    model = Tecnico
    form_class = TecnicoForm
    template_name = "Tecnicos/crear.html"
    success_url = reverse_lazy("apl:tecnico_listar")
    entidad = "tecnico"

class TecnicoDeleteView(BaseDeleteView):
    model = Tecnico
    template_name = "Tecnicos/eliminar.html"
    success_url = reverse_lazy("apl:tecnico_listar")
    entidad = "tecnico"

# ===================== Orden de Servicio =====================

class OrdenServicioListView(BaseListView):
    model = OrdenServicio
    template_name = "Orden_Servicio/listar_orden_servicio.html"
    context_object_name = "ordenes"
    entidad = "ordenservicio"

class OrdenServicioCreateView(BaseCreateView):
    model = OrdenServicio
    form_class = OrdenServicioForm
    template_name = "Orden_Servicio/crear.html"
    success_url = reverse_lazy("apl:ordenservicio_listar")
    entidad = "ordenservicio"

class OrdenServicioUpdateView(BaseUpdateView):
    model = OrdenServicio
    form_class = OrdenServicioForm
    template_name = "Orden_Servicio/crear.html"
    success_url = reverse_lazy("apl:ordenservicio_listar")
    entidad = "ordenservicio"

class OrdenServicioDeleteView(BaseDeleteView):
    model = OrdenServicio
    template_name = "Orden_Servicio/eliminar.html"
    success_url = reverse_lazy("apl:ordenservicio_listar")
    entidad = "ordenservicio"

# ===================== Servicio Tecnico =====================

class ServicioTecnicoListView(BaseListView):
    model = ServicioTecnico
    template_name = "Servicio_Tecnico/listar_servicio_tecnico.html"
    context_object_name = "servicios"
    entidad = "serviciotecnico"

class ServicioTecnicoCreateView(BaseCreateView):
    model = ServicioTecnico
    form_class = ServicioTecnicoForm
    template_name = "Servicio_Tecnico/crear.html"
    success_url = reverse_lazy("apl:serviciotecnico_listar")
    entidad = "serviciotecnico"

class ServicioTecnicoUpdateView(BaseUpdateView):
    model = ServicioTecnico
    form_class = ServicioTecnicoForm
    template_name = "Servicio_Tecnico/crear.html"
    success_url = reverse_lazy("apl:serviciotecnico_listar")
    entidad = "serviciotecnico"

class ServicioTecnicoDeleteView(BaseDeleteView):
    model = ServicioTecnico
    template_name = "Servicio_Tecnico/eliminar.html"
    success_url = reverse_lazy("apl:serviciotecnico_listar")
    entidad = "serviciotecnico"

# ===================== Venta =====================

class VentaListView(BaseListView):
    model = Venta
    template_name = "Ventas/listar_ventas.html"
    context_object_name = "ventas"
    entidad = "venta"

class VentaCreateView(BaseCreateView):
    model = Venta
    form_class = VentaForm
    template_name = "Ventas/crear.html"
    success_url = reverse_lazy("apl:venta_listar")
    entidad = "venta"

class VentaUpdateView(BaseUpdateView):
    model = Venta
    form_class = VentaForm
    template_name = "Ventas/crear.html"
    success_url = reverse_lazy("apl:venta_listar")
    entidad = "venta"

class VentaDeleteView(BaseDeleteView):
    model = Venta
    template_name = "Ventas/eliminar.html"
    success_url = reverse_lazy("apl:venta_listar")
    entidad = "venta"

# ===================== Compras Mercancia =====================
class ComprasMercanciaListView(BaseListView):
    model = ComprasMercancia
    template_name = 'Compras_Mercancia/listar_compras_mercancia.html'
    context_object_name = 'compras'
    entidad = 'comprasmercancia'

class ComprasMercanciaCreateView(BaseCreateView):
    model = ComprasMercancia
    form_class = ComprasMercanciaForm
    template_name = 'Compras_Mercancia/crear.html'
    success_url = reverse_lazy('apl:comprasmercancia_listar')
    entidad = 'comprasmercancia'

class ComprasMercanciaUpdateView(BaseUpdateView):
    model = ComprasMercancia
    form_class = ComprasMercanciaForm
    template_name = 'Compras_Mercancia/crear.html'
    success_url = reverse_lazy('apl:comprasmercancia_listar')
    entidad = 'comprasmercancia'

class ComprasMercanciaDeleteView(BaseDeleteView):
    model = ComprasMercancia
    template_name = 'Compras_Mercancia/eliminar.html'
    success_url = reverse_lazy('apl:comprasmercancia_listar')
    entidad = 'comprasmercancia'

# ===================== Garantias =====================

class GarantiasListView(BaseListView):
    model = Garantias
    template_name = "Garantias/listar_garantias.html"
    context_object_name = "garantias"
    entidad = "garantias"

class GarantiasCreateView(BaseCreateView):
    model = Garantias
    form_class = GarantiasForm
    template_name = "Garantias/crear.html"
    success_url = reverse_lazy("apl:garantias_listar")
    entidad = "garantias"

class GarantiasUpdateView(BaseUpdateView):
    model = Garantias
    form_class = GarantiasForm
    template_name = "Garantias/crear.html"
    success_url = reverse_lazy("apl:garantias_listar")
    entidad = "garantias"

class GarantiasDeleteView(BaseDeleteView):
    model = Garantias
    template_name = "Garantias/eliminar.html"
    success_url = reverse_lazy("apl:garantias_listar")
    entidad = "garantias"