from django import views
from django.urls import path
from casa.views import *
from casa import views


urlpatterns = [
    
    #URLS de la tabla propietarios
    
    path('guardar_propietario/', views.FormularioPropietarioView.procesar_formulario, name='guardar_propietario'),
    
    path('actualizar_propietario/<int:id_propietario>', views.FormularioPropietarioView.actualizar_propietario, name='actualizarpropietario'),
    path('eliminar_propietario/<int:pk>', EliminarPropietario.as_view(), name='eliminarpropietario'),
    path('listar_propietarios/', ListarPropietarios.as_view(), name='propietarios'),
    path('registrar_propietario/', RegistrarPropietario.as_view(), name='registrarpropietario'),
    path('editar_propietario/<int:pk>', ActualizarPropietario.as_view(), name='editarpropietario'),


    #URLS de la tabla inquilinos
    path('registrarinquilinos/', views.FormularioInquilinoView.index, name='registrarinquilinos'),
    path('guardarinquilinos/', views.FormularioInquilinoView.procesar_formulario, name='guardar_inquilino'),
    path('editar_inquilino/<int:id_inquilino>', views.FormularioInquilinoView.editar_inquilino, name='editarinquilino'),
    path('actualizar_inquilino/<int:id_inquilino>', views.FormularioInquilinoView.actualizar_inquilino, name='actualizarinquilino'),
    path('eliminar_inquilino/<int:pk>', EliminarInquilino.as_view(), name='eliminarinquilino'),
    path('listar_inquilinos/', ListarInquilinos.as_view(), name='inquilinos'),


    #URLS de la tabla casas
    
    path('editar_casa/<int:id_casa>', views.FormularioCasaView.editar_casa, name='editarcasa'),
    path('actualizar_casa/<int:id_casa>', views.FormularioCasaView.actualizar_casa, name='actualizarcasa'),
    path('listar_casas/', ListarCasas.as_view(), name='listado_casas'),

]

