from django.urls import path
from . import views

urlpatterns = [
    # Administrador
    path("administradores/", views.AdministradorList.as_view(), name="administrador_list"),
    path("administradores/nuevo/", views.AdministradorCreate.as_view(), name="administrador_create"),
    path("administradores/<int:pk>/editar/", views.AdministradorUpdate.as_view(), name="administrador_update"),
    path("administradores/<int:pk>/eliminar/", views.AdministradorDelete.as_view(), name="administrador_delete"),
]
