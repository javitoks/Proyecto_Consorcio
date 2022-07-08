from django.contrib import admin

from casa.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

#Para que aparezcan los campos "created" y "updated" y decirle q son de SOLO LECTURA, tenemos que crear una clase:

#Administracion de Casas

class ExportarImportarCasa(resources.ModelResource):
    
    fields = (
        'numero_casa',
        'propietario', 
        'inquilino',
    )
    
    class Meta:
        model = Casa

class CasaAdmin(ImportExportModelAdmin):
    resource_class = ExportarImportarCasa
    
    icon_name = 'location_city'

    readonly_fields = (
        'creado', 
        'modificado'
        )
    list_display = (
        'numero_casa',
        'propietario', 
        'inquilino'
        )
    ordering = (
        'propietario', 
        'inquilino', 
        'numero_casa'
        )
    search_fields = (
        'propietario', 
        'inquilino'
        )
    #date_hierarchy = 'creado'

#Administracion de Inquilinos

class ExportarImportarInquilinos(resources.ModelResource):
    
    fields = (
        'nombre', 
        'apellido', 
        'telefono', 
        'email', 
        'vigencia',
    )
    
    class Meta:
        model = Inquilino

class InquilinoAdmin(ImportExportModelAdmin):
   
    resource_class =  ExportarImportarInquilinos

    icon_name = 'face'
   
    readonly_fields = (
        'creado', 
        'modificado'
        )
    list_display = (
        'nombre', 
        'apellido', 
        'telefono', 
        'email', 
        'vigencia'
        )
    ordering = (
        'nombre', 
        'apellido'
        )
    search_fields = (
        'nombre', 
        'apellido'
        )

#Administracion de Propietarios

class ExportarImportarPropietario(resources.ModelResource):
    fields = (
        'nombre',
        'apellido', 
        'telefono', 
        'email', 
        'CBU'
    )
    
    class Meta:
        model = Propietario


class PropietarioAdmin(ImportExportModelAdmin):
    
    resource_class = ExportarImportarPropietario
    
    icon_name = 'assignment_ind'

    readonly_fields = (
        'creado', 
        'modificado'
        )
    list_display = (
        'nombre',
        'apellido', 
        'telefono', 
        'email', 
        'CBU'
        )
    ordering = (
        'nombre', 
        'apellido'
        )
    search_fields = (
        'nombre', 
        'apellido'
        )

#Administracion de Administradores

class ExportarImportarAdministradores(resources.ModelResource):
    
    fields = (
        'nombre', 
        'apellido', 
        'telefono', 
        'email',
    )
    
    class Meta:
        model = Administrador

class AdministradorAdmin(ImportExportModelAdmin):
    
    resource_class = ExportarImportarAdministradores

    icon_name = 'group'
    
    readonly_fields = (
        'creado', 
        'modificado'
        )
    list_display = (
        'nombre', 
        'apellido', 
        'telefono', 
        'email'
        )

#Administracion de Cuotas

class ExportarImportarCuotas(resources.ModelResource):
    
    fields = (
        'mes', 
        'año', 
        'monto',
    )
    
    class Meta:
        model = Cuota

class CuotaAdmin(ImportExportModelAdmin):
    
    resource_class = ExportarImportarCuotas

    icon_name = 'assignment'
    
    readonly_fields = (
        'creado', 
        'modificado'
        )
    list_display = (
        'mes', 
        'año', 
        'monto'
        )
    search_fields = (
        'mes', 
        'año'
        )

class PagoAdmin(ImportExportModelAdmin):
    
    icon_name = 'attach_money'

    list_display = ('propietario', 'cuota_abonada')



admin.site.register(Casa, CasaAdmin)
admin.site.register(Inquilino, InquilinoAdmin)
admin.site.register(Propietario, PropietarioAdmin)
admin.site.register(Administrador, AdministradorAdmin)
admin.site.register(Cuota, CuotaAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.site_header = 'Consorcio Rivadavia'
admin.site.index_title = 'Administracion de Consorcio Rivadavia'
admin.site.site_title = 'Consorcio Rivadavia'