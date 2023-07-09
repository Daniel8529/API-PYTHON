from django.db import models

# Create your models here.
class Usuarios(models.Model):
     Nombre = models.CharField(max_length=100)
     NombreUsuario=models.CharField(max_length=60)
     Correo=models.CharField(max_length=90)
     Password=models.PositiveSmallIntegerField()

class Eventos(models.Model):
    Nombre = models.CharField(max_length=100)
    Fecha = models.CharField(max_length=50)
    Tipo=models.CharField(max_length=60)
    Image= models.CharField(max_length=500)
    Ciudad= models.CharField(max_length=50)
    Lugar=models.CharField(max_length=50)
    Cantidad= models.PositiveSmallIntegerField()
    
class Secciones(models.Model):
     IdEvento = models.CharField(max_length=100)
     Tipo=models.CharField(max_length=60)
     Secciones=models.CharField(max_length=60)
     Is_active=models.BooleanField(default=False)
     


   

