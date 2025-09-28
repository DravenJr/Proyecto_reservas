from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

User = get_user_model()


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "api/dashboard.html"
    login_url = '/auth/login/'


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return render(request, "api/register.html")

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            {"message": "Usuario creado con éxito"},
            status=status.HTTP_201_CREATED
        )


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


class HomeView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return render(request, "api/index.html")
