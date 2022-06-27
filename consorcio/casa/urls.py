from django import views
from django.contrib import admin
from django.urls import path
from casa import views


urlpatterns = [
    
    #URLS de la tabla propietarios
    path('registrar_propietario/', views.FormularioPropietarioView.index, name='registrarpropietario'),
    path('guardar_propietario/', views.FormularioPropietarioView.procesar_formulario, name='guardar_propietario'),
    path('propietarios/', views.FormularioPropietarioView.listado_propietarios, name='propietarios'),
    path('editar_propietario/<int:id_propietario>', views.FormularioPropietarioView.editar_propietario, name='editarpropietario'),
    path('actualizar_propietario/<int:id_propietario>', views.FormularioPropietarioView.actualizar_propietario, name='actualizarpropietario'),



    #URLS de la tabla inquilinos
    path('inquilinos/', views.FormularioInquilinoView.listado_inquilinos, name='inquilinos'),
    path('registrarinquilinos/', views.FormularioInquilinoView.index, name='registrarinquilinos'),
    path('guardarinquilinos/', views.FormularioInquilinoView.procesar_formulario, name='guardar_inquilino'),
    path('actualizar_inquilino/<int:id_inquilino>', views.FormularioInquilinoView.editar_inquilino, name='actualizarinquilino'),


    path('casas/', views.FormularioPropietarioView.listado_casas, name='listado_casas'),
    



]

