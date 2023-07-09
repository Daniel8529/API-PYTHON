from django.urls import path, include
from rest_framework import routers
from apiApp import views

router = routers.DefaultRouter()
router.register(r'Eventos', views.EventosViewSet)
router.register(r'Secciones', views.SeccionesViewSet)
router.register(r'Usuarios', views.UsuariosViewSet)

urlpatterns = [
    path('', include(router.urls))
]
