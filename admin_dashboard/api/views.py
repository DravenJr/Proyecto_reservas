
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions

@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def stats_reservas_por_cancha(request):
   
    return Response({'message': 'Aquí debe ir el conteo de reservas por cancha (implementación)'} )

@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def usuarios_registrados(request):
    return Response({'message': 'Aquí lista de usuarios (implementar consulta a auth_service)'} )
