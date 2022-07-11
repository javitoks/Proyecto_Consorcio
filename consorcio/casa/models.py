from django.db import models

# Create your models here.  




class Administrador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30, blank=True)
    telefono = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)
    creado = models.DateTimeField(auto_now_add=True) 
    modificado = models.DateTimeField(auto_now=True)

   
    class Meta:
        verbose_name = ("Administrador")
        verbose_name_plural = ("Administradores")
    
    def __str__(self):
        return ('{} {}'.format(self.apellido, self.nombre))
    

class Propietario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30, blank=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    CBU = models.CharField(max_length=22, blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True) 
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nombre']   
        verbose_name = 'Propietarios'
        verbose_name_plural = "Propietarios"
    
    def __str__(self):
        return ('{} {}'.format(self.apellido, self.nombre))
        

class Inquilino(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30, blank=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    CBU = models.CharField(max_length=22, blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True) 
    modificado = models.DateTimeField(auto_now=True)
    vigencia = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['nombre']
        verbose_name = ("Inquilino")
        verbose_name_plural = ("Inquilinos")
    
    def __str__(self):


        return ('{} {}'.format(self.apellido, self.nombre))


class Casa(models.Model):
    numero_casa = models.CharField(max_length=2, blank=False, null=False, help_text='Ingrese el numero y la letra ej: 5A')
    propietario = models.ForeignKey(Propietario, on_delete=models.RESTRICT)  
    administrador = models.ForeignKey(Administrador, on_delete=models.RESTRICT) 
    opciones_estado = [
        ('Alquilada', 'Alquilada'), 
        ('Desocupada' , 'Desocupada') , 
        ('Ocupada-Dueño', 'Ocupada-Dueño')
        ]
    estado = models.CharField(max_length=15, null=False, choices=opciones_estado, default='OCU')
    inquilino = models.ForeignKey(Inquilino, verbose_name=("Inquilino"), on_delete=models.RESTRICT)
    disponibilidad = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True) 
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['numero_casa']
        verbose_name = ("Casa")
        verbose_name_plural = ("Casas")
    

        

class Cuota(models.Model):
    meses = [
        ('01','Enero'),
        ('Febrero','Febrero'),
        ('Marzo','Marzo'),
        ('Abril','Abril'),
        ('Mayo','Mayo'),
        ('Junio','Junio'),
        ('Julio','Julio'),
        ('Agosto','Agosto'),
        ('Septiembre','Septiembre'),
        ('Octubre','Octubre'),
        ('Noviembre','Noviembre'),
        ('Diciembre','Diciembre')        
    ]
    mes =  models.CharField(max_length=15, null=False, choices=meses, default='enero')
    monto = models.IntegerField()
    año = models.PositiveSmallIntegerField(default=2022)
    creado = models.DateTimeField(auto_now_add=True) 
    modificado = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ['mes']
        verbose_name = ("Cuota")
        verbose_name_plural = ("Cuotas")
    
    def __str__(self):
        return ('{} {} {}'.format(self.mes, 'de', self.año))


class Pago(models.Model):
    propietario = models.ForeignKey(Propietario, verbose_name= ("Propietario"), on_delete=models.CASCADE)
    cuota_abonada = models.ForeignKey(Cuota, verbose_name= ("Cuota"), on_delete=models.CASCADE)
    casa = models.ForeignKey(Casa, verbose_name=('Casa'), on_delete=models.CASCADE)

    class Meta:
        ordering = ['casa']
        verbose_name = ("Pago")
        verbose_name_plural = ("Pagos")
    
    def __str__(self):
        return ('{} {} {}'.format(self.propietario, '-', self.cuota_abonada))

