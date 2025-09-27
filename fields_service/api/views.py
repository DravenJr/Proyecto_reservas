from rest_framework import viewsets, permissions
from .models import Field
from .serializers import FieldSerializer

#API REST de canchas
class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
