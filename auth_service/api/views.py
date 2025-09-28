from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "api/dashboard.html"
    login_url = '/login/'

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return render(request, "api/register.html")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return redirect('dashboard')

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    # Mostrar formulario HTML
    def get(self, request):
        return render(request, "api/register.html")

    # Sobrescribir create para redirigir después de registro
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Aquí rediriges al dashboard (puedes usar nombre de url)
        return redirect('dashboard')  # 'dashboard' es el name de tu path

        # Si quieres devolver JSON en vez de redirigir, podrías usar:
        # return Response(serializer.data, status=status.HTTP_201_CREATED)


#Perfil
class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

#Home público
class HomeView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return render(request, "api/index.html")
