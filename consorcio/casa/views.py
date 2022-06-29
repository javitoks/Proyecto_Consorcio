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
    success_url = reverse_lazy('propietarios')      


class ListarPropietarios(ListView):
    model = Propietario                             
    template_name = "propietarios.html"

class ActualizarPropietario(UpdateView):            
    model = Propietario
    template_name = "editarpropietario.html"
    form_class = FormularioPropietario
    success_url = reverse_lazy('propietarios')


#INQUILINOS

class RegistrarInquilino(CreateView):
    model = Inquilino
    form_class = FormularioInquilino
    template_name = "registrarinquilino.html"     
    success_url = reverse_lazy('inquilinos')


class ActualizarInquilino(UpdateView):            
    model = Inquilino
    template_name = "editarinquilino.html"
    form_class = FormularioInquilino
    success_url = reverse_lazy('inquilinos')


class EliminarInquilino(DeleteView):
    model = Inquilino
    template_name = "inquilino_eliminar.html"
    success_url = reverse_lazy('inquilinos')

class ListarInquilinos(ListView):
    model = Inquilino
    template_name = "inquilinos.html"

#CASA

class ListarCasas(ListView):
    model = Casa
    template_name = "listado_casas.html"

class ActualizarCasa(UpdateView):            
    model = Casa
    template_name = "editarcasa.html"
    form_class = FormularioCasa
    success_url = reverse_lazy('listado_casas')


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
