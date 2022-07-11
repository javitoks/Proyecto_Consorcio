from django import views
from django.urls import path
from casa.views import *
from casa import views


urlpatterns = [
    
    #URLS de la tabla propietarios

    path('eliminar_propietario/<int:pk>', EliminarPropietario.as_view(), name='eliminarpropietario'),
    path('listar_propietarios/', ListarPropietarios.as_view(), name='propietarios'),
    path('registrar_propietario/', RegistrarPropietario.as_view(), name='registrarpropietario'),
    path('editar_propietario/<int:pk>', ActualizarPropietario.as_view(), name='editarpropietario'),
    path('reporte_propietarios/', ExportarPropietarios.as_view(), name='reportepropietarios'),
    




    #URLS de la tabla inquilinos
    
    path('eliminar_inquilino/<int:pk>', EliminarInquilino.as_view(), name='eliminarinquilino'),
    path('listar_inquilinos/', ListarInquilinos.as_view(), name='inquilinos'),
    path('registrar_inquilinos/', RegistrarInquilino.as_view(), name='registrarinquilinos'),
    path('editar_inquilino/<int:pk>', ActualizarInquilino.as_view(), name='editarinquilino'),
 

    #URLS de la tabla casas
    
    path('listar_casas/', ListarCasas.as_view(), name='listado_casas'),
    path('actualizar_casa/<int:pk>', ActualizarCasa.as_view(), name='actualizarcasa'),


    #Pagos
    path('cupones_pago/', ListarCupones.as_view(), name='cuponespago'),

    path('listar_pagos/', ListarPagos.as_view(), name='listarpagos'),
    path('registrar_pagos/', RegistrarPago.as_view(), name='registrarpago'),




]

