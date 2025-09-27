from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, HomeView

router = DefaultRouter()
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('api/', include(router.urls)),
]
