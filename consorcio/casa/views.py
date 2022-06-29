from venv import create
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from casa.forms import *
from casa.models import *

from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic import ListView


# Create your views here.

#PROPIETARIOS

class RegistrarPropietario(CreateView):
    model = Propietario
    form_class = FormularioPropietario
    template_name = "registrarpropietario.html"
    success_url = reverse_lazy('propietarios')

class EliminarPropietario(DeleteView):
    model = Propietario
    template_name = "propietario_eliminar.html"
    success_url = reverse_lazy('propietarios')      #OK


class ListarPropietarios(ListView):
    model = Propietario                             #OK
    template_name = "propietarios.html"

class ActualizarPropietario(UpdateView):            #OK
    model = Propietario
    template_name = "editarpropietario.html"
    form_class = FormularioPropietario
    success_url = reverse_lazy('propietarios')
            

#INQUILINOS

class EliminarInquilino(DeleteView):
    model = Inquilino
    template_name = "inquilino_eliminar.html"
    success_url = reverse_lazy('inquilinos')

class ListarInquilinos(ListView):
    model = Inquilino
    template_name = "inquilinos.html"

class FormularioInquilinoView(HttpRequest):

    def index(request):
        inquilino = FormularioInquilino()
        return render(request, 'registrarinquilino.html', {'form': inquilino})


    def procesar_formulario(request):
        inquilino = FormularioInquilino(request.POST)
        if inquilino.is_valid():
            inquilino.save()
            inquilino = FormularioInquilino()
        return render(request, 'registrarinquilino.html', {'form': inquilino, 'mensaje': 'OK'})

    def editar_inquilino(request, id_inquilino):
        inquilino = Propietario.objects.filter(id=id_inquilino).first()
        form = FormularioPropietario(instance = inquilino)
        return render(request, 'editarinquilino.html', {'form':form, 'inquilino':inquilino})

    def actualizar_inquilino(request, id_inquilino):
        inquilino = Inquilino.objects.get(pk=id_inquilino)
        form = FormularioInquilino(request.POST, instance=inquilino)
        if form.is_valid():
            form.save()
        inquilinos = Inquilino.objects.all()
        return render(request, 'inquilinos.html', {'inquilinos': inquilinos})


#CASA

class ListarCasas(ListView):
    model = Casa
    template_name = "listado_casas.html"


class FormularioCasaView(HttpRequest):

    def editar_casa(request, id_casa):
        casa = Casa.objects.filter(id=id_casa).first()
        form = FormularioCasa(instance = casa)
        return render(request, 'editarcasa.html', {'form':form, 'casa':casa})

    def actualizar_casa(request, id_casa):
        casa = Casa.objects.get(pk=id_casa)
        form = FormularioCasa(request.POST, instance=casa)
        if form.is_valid():
            form.save()
        casas = Casa.objects.all()
        return render(request, 'listado_casas.html', {'casas': casas})
