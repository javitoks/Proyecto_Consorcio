from django.http import HttpRequest
from django.shortcuts import render
from casa.forms import FormularioPropietario
from casa.models import Casa, Inquilino, Propietario

# Create your views here.


class FormularioPropietarioView(HttpRequest):

    def index(request):
        propietario = FormularioPropietario()
        return render(request, 'registrarpropietario.html', {'form': propietario})

    def procesar_formulario(request):
        propietario = FormularioPropietario(request.POST)
        if propietario.is_valid():
            propietario.save()
            propietario = FormularioPropietario()
        return render(request, 'registrarpropietario.html', {'form': propietario, 'mensaje': 'OK'})

    def editar_propietario(request, id_propietario):
        propietario = Propietario.objects.filter(id=id_propietario).first()
        form = FormularioPropietario(instance = propietario)
        return render(request, 'editarpropietario.html', {'form':form, 'propietario':propietario})

    def actualizar_propietario(request, id_propietario):
        propietario = Propietario.objects.get(pk=id_propietario)
        form = FormularioPropietario(request.POST, instance=propietario)
        if form.is_valid():
            form.save()
        propietarios = Propietario.objects.all()
        return render(request, 'propietarios.html', {'propietarios': propietarios})
    
    
    
    #por ahora estan aca
    
    def listado_propietarios(request):
        data = {
            'titulo': 'Listado de Propietarios',
            'propietarios': Propietario.objects.all()
        }
        return render(request, 'propietarios.html', data)

    def listado_casas(request):
        data = {
            'titulo': 'Listado de Casas',
            'casas': Casa.objects.all()
        }
        return render(request, 'listado_casas.html', data)

    def listado_inquilinos(request):
        data = {
            'titulo': 'Listado de Propietarios',
            'inquilinos': Inquilino.objects.all()
        }
        return render(request, 'inquilinos.html', data)
