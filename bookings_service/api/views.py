from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Booking
from .serializers import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('-start')
    serializer_class = BookingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Booking.objects.all().order_by('-start')
        return Booking.objects.filter(user_id=user.id).order_by('-start')

    def list(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(
                {"detail": "Necesitas estar logueado para acceder a este servicio."}, 
                status=403
            )
        return super().list(request, *args, **kwargs)
