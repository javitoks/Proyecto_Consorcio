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
    path('eliminar_propietario/<int:id_propietario>', views.FormularioPropietarioView.eliminar_propietario, name='eliminarpropietario'),


    #URLS de la tabla inquilinos
    path('inquilinos/', views.FormularioInquilinoView.listado_inquilinos, name='inquilinos'),
    path('registrarinquilinos/', views.FormularioInquilinoView.index, name='registrarinquilinos'),
    path('guardarinquilinos/', views.FormularioInquilinoView.procesar_formulario, name='guardar_inquilino'),
    path('editar_inquilino/<int:id_inquilino>', views.FormularioInquilinoView.editar_inquilino, name='editarinquilino'),
    path('actualizar_inquilino/<int:id_inquilino>', views.FormularioInquilinoView.actualizar_inquilino, name='actualizarinquilino'),

    #URLS de la tabla casas
    path('casas/', views.FormularioCasaView.listado_casas, name='listado_casas'),
    path('editar_casa/<int:id_casa>', views.FormularioCasaView.editar_casa, name='editarcasa'),
    path('actualizar_casa/<int:id_casa>', views.FormularioCasaView.actualizar_casa, name='actualizarcasa'),




]

