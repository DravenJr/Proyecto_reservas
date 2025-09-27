from rest_framework import viewsets, permissions
from django.shortcuts import render
from .models import Booking
from .serializers import BookingSerializer

class HomeView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return render(request, "booking_index.html")

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('-start')
    serializer_class = BookingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Booking.objects.all().order_by('-start')
        return Booking.objects.filter(user_id=user.id).order_by('-start')
