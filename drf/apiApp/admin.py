from django.contrib import admin
from .models import Eventos
from .models import Secciones
from .models import Usuarios

# Register your models here.

admin.site.register(Eventos)
admin.site.register(Secciones)
admin.site.register(Usuarios)

