from django import views
from django.contrib import admin
from django.urls import path
from casa import views


urlpatterns = [
    #path('casas/', views.listado_casas, name='listado_casas'),
    #path('propietarios/', views.listado_propietarios, name='propietarios'),
    #path('inquilinos/', views.listado_inquilinos, name='inquilinos'),

    path('registrar_propietario/', views.FormularioPropietarioView.index, name='registrarpropietario'),
    path('guardar_propietario/', views.FormularioPropietarioView.procesar_formulario, name='guardar_propietario'),
    path('propietarios/', views.FormularioPropietarioView.listado_propietarios, name='propietarios'),
    path('casas/', views.FormularioPropietarioView.listado_casas, name='listado_casas'),
    path('inquilinos/', views.FormularioPropietarioView.listado_inquilinos, name='inquilinos'),
    path('editar_propietario/<int:id_propietario>', views.FormularioPropietarioView.editar_propietario, name='editarpropietario'),
    path('actualizar_propietario/<int:id_propietario>', views.FormularioPropietarioView.actualizar_propietario, name='actualizarpropietario')







]

