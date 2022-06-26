from http.client import ImproperConnectionState
from django.shortcuts import render
from casa.models import Casa

# Create your views here.


def listado_casas(request):
    data = {
        'titulo' : 'Listado de Casas',
        'casas' : Casa.objects.all()
        }
    return render(request, 'listado_casas.html', data)

