from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, HomeView

router = DefaultRouter()
router.register('bookings', BookingViewSet)

urlpatterns = [
    path('', HomeView.as_view(), name='api_home'),
    path('', include(router.urls)),
]
