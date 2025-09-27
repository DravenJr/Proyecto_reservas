from rest_framework import viewsets, permissions
from .models import Field
from .serializers import FieldSerializer
from django.shortcuts import render

# API REST de canchas
class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

def listar_canchas(request):
    return render(request, 'fields_list.html')
