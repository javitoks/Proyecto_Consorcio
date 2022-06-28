from venv import create
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from casa.forms import FormularioPropietario, FormularioInquilino, FormularioCasa
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
    success_url = reverse_lazy('propietarios')


class ListarPropietarios(ListView):
    model = Propietario
    template_name = "propietarios.html"

class ActualizarPropietario(UpdateView):
    model = Propietario
    template_name = "editarpropietario.html"
    form_class = FormularioPropietario
    success_url = 'propietarios.html'




class FormularioPropietarioView(HttpRequest):

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
