from django.db import models

# Create your models here.




class Administrador(models.Model):
    nombre = models.CharField(max_length=30, blank=False)
    apellido = models.CharField(max_length=30, blank=False)
    telefono = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)
    #administradas = models.ManyToManyField(Casa)

   
    class Meta:
        verbose_name = ("Administrador")
        verbose_name_plural = ("Administradores")
    
        def __str__(self):
            return self.nombre
    

class Propietario(models.Model):
    nombre = models.CharField(max_length=30, blank=False)
    apellido = models.CharField(max_length=30, blank=False)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    CBU = models.CharField(max_length=22, blank=True, null=True)
    #propiedades = models.ManyToManyField(Casa)

    class Meta:
        verbose_name = ("Propietario")
        verbose_name_plural = ("Propietarios")
    
        def __str__(self):
            return self.nombre

class Inquilino(models.Model):
    nombre = models.CharField(max_length=30, blank=False)
    apellido = models.CharField(max_length=30, blank=False)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    CBU = models.CharField(max_length=22, blank=True, null=True)
    
    class Meta:
        verbose_name = ("Inquilino")
        verbose_name_plural = ("Inquilinos")
    
        def __str__(self):
            return self.nombre


class Casa(models.Model):
    numero_casa = models.CharField(max_length=2, blank=False, null=False, help_text='Ingrese el numero y la letra ej: 5A')
    propietario = models.ForeignKey(Propietario, verbose_name=("Propietario"), on_delete=models.CASCADE)
    administrador = models.ForeignKey(Administrador, verbose_name=("Administrador"), on_delete=models.CASCADE)
    opciones_estado = [('ALQ', 'Alquilada'), ('DES' , 'Desocupada') , ('OCU', 'Ocupada-Dueño')]
    estado = models.BooleanField(null=False, choices=opciones_estado, default='OCU')
    inquilino = models.ForeignKey(Inquilino, verbose_name=("Inquilino"), on_delete=models.CASCADE)     