from django.urls import path
from .views import RegisterView, ProfileView, HomeView, DashboardView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', HomeView.as_view(), name='auth_home'),
    path('auth/register/', RegisterView.as_view(), name='register'),   # <- cambiado
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # <- cambiado
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', ProfileView.as_view(), name='profile'),
    path('auth/dashboard/', DashboardView.as_view(), name='dashboard')  # <- cambiado
]
