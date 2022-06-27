from django.contrib import admin
from casa.models import *

# Register your models here.

#Para que aparezcan los campos "created" y "updated" y decirle q son de SOLO LECTURA, tenemos que crear una clase:

class CasaAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')

class InquilinoAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')

class PropietarioAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')

class AdministradorAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')


admin.site.register(Casa, CasaAdmin)
admin.site.register(Inquilino, InquilinoAdmin)
admin.site.register(Propietario)
admin.site.register(Administrador, AdministradorAdmin)