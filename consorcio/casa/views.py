from django.http import HttpRequest
from django.shortcuts import render
from casa.forms import FormularioPropietario, FormularioInquilino, FormularioCasa
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
   
    def listado_propietarios(request):
        data = {
            'titulo': 'Listado de Propietarios',
            'propietarios': Propietario.objects.all()
        }
        return render(request, 'propietarios.html', data)


    def eliminar_propietario(request, id_propietario):
        propietario = Propietario.objects.get(pk=id_propietario)
        propietario.delete()
        propietarios = Propietario.objects.all()
        propietarios = Propietario.objects.all()
        return render(request, 'propietarios.html', {'propietarios': propietarios})
        



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


    def listado_inquilinos(request):
        data = {
            'titulo': 'Listado de Inquilinos',
            'inquilinos': Inquilino.objects.all()
        }
        return render(request, 'inquilinos.html', data)

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


    def listado_casas(request):
        data = {
            'titulo': 'Listado de Casas',
            'casas': Casa.objects.all()
        }
        return render(request, 'listado_casas.html', data)