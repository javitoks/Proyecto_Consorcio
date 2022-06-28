from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'home.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('home')


def logueo(request):     #El get nos muestra el form
        form = AuthenticationForm()
        return render (request, 'login.html', {'form': form})


def loguearse(request):
    if request.method=='POST':    #Si se pulso el boton (al pulsar el boton, envia un metodo post con la info del form)
        form = AuthenticationForm(request, data=request.POST) #guardar en form los datos ingresados por el usuario
        if form.is_valid():     #si el form es valido (correcto)
            nombre_usuario = form.cleaned_data.get('username')  #cargar en nombre_usuario lo que el usuario cargo en el username
            contraseña = form.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=contraseña)    #comprueba que lo que ingreso el usuario se corresponde con lo que hay en la base
            if usuario is not None: #si nos devuelve un usuario correctamente (si estuviera mal no nos devolveria nada)
                login(request, usuario) #que se loguee utilizando lo almacenado en usuario
                return redirect('home')

            else:
                messages.error(request, 'La informacion ingresada es incorrecta')    #si hay algun error, sale este mensaje
        else:
            messages.error(request, 'La informacion ingresada es incorrecta')
    
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
