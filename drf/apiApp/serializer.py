from rest_framework import serializers
from .models import Eventos
from .models import Secciones
from .models import Usuarios

        
class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuarios
        
        # fields = ('fullname', 'nickname')
        fields = '__all__'

class EventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eventos
        
        # fields = ('fullname', 'nickname')
        fields = '__all__'

class SeccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Secciones
        
        # fields = ('fullname', 'nickname')
        fields = '__all__'
