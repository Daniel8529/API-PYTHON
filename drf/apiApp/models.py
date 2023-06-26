from django.db import models

# Create your models here.

class Eventos(models.Model):
    Nombre = models.CharField(max_length=100)
    Fecha = models.CharField(max_length=50)
    Tipo=models.CharField(max_length=60)
    Image= models.CharField(max_length=500)
    Ciudad= models.CharField(max_length=50)
    Lugar=models.CharField(max_length=50)
    Cantidad= models.PositiveSmallIntegerField()
    
class Secciones(models.Model):
     idEvento = models.CharField(max_length=100)
     Tipo=models.CharField(max_length=60)
     secciones=models.CharField(max_length=60)

   

