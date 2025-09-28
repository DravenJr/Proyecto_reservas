from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FieldViewSet

#Configuración del router para la API
router = DefaultRouter()
router.register('fields', FieldViewSet)

urlpatterns = [
    #API REST
    path('api/', include(router.urls)),
]
