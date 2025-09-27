from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FieldViewSet, listar_canchas

# Configuración del router para la API
router = DefaultRouter()
router.register('fields', FieldViewSet)

urlpatterns = [
    # API REST
    path('api/', include(router.urls)),

    # HTML con la lista de canchas
    path('canchas/', listar_canchas, name='listar_canchas'),
]
