from django.shortcuts import render
from casa.models import Casa, Inquilino, Propietario

# Create your views here.


def listado_casas(request):
    data = {
        'titulo': 'Listado de Casas',
        'casas': Casa.objects.all()
    }
    return render(request, 'listado_casas.html', data)

def listado_propietarios(request):
    data = {
        'titulo': 'Listado de Propietarios',
        'propietarios': Propietario.objects.all()
    }
    return render(request, 'propietarios.html', data)

def listado_inquilinos(request):
    data = {
        'titulo': 'Listado de Propietarios',
        'inquilinos': Inquilino.objects.all()
    }
    return render(request, 'inquilinos.html', data)