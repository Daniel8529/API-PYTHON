from rest_framework import serializers
from .models import Eventos
from .models import Secciones


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
