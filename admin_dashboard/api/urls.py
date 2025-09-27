
from django.urls import path
from .views import stats_reservas_por_cancha, usuarios_registrados

urlpatterns = [
    path('stats/reservas-por-cancha/', stats_reservas_por_cancha),
    path('users/', usuarios_registrados),
]
