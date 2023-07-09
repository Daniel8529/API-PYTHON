from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuarios
from .models import Eventos
from .models import Secciones
from .serializer import UsuariosSerializer
from .serializer import EventosSerializer
from .serializer import SeccionesSerializer


# Create your views here.
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class EventosViewSet(viewsets.ModelViewSet):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer

class SeccionesViewSet(viewsets.ModelViewSet):
    queryset = Secciones.objects.all()
    serializer_class = SeccionesSerializer

