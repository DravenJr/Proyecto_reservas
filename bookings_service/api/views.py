from rest_framework import viewsets, permissions, generics
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Booking
from .serializers import BookingSerializer

# Vista de inicio / API Gateway
class HomeView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return render(request, "index.html")


# ViewSet de la API de bookings
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('-start')
    serializer_class = BookingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Booking.objects.all().order_by('-start')
        return Booking.objects.filter(user_id=user.id).order_by('-start')


# Vista HTML de bookings que redirige si no está autenticado
def bookings_page(request):
    if not request.user.is_authenticated:
        # Mensaje de alerta y redirección al api_gateway
        messages.warning(request, "Necesitas estar logueado para acceder a este servicio")
        return redirect('/')  # Ajusta la URL según tu página principal

    # Si está logueado, obtiene las reservas
    user = request.user
    bookings = Booking.objects.all() if user.is_staff else Booking.objects.filter(user=user)
    return render(request, "bookings.html", {"bookings": bookings})
