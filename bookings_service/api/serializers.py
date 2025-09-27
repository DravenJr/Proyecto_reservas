
from rest_framework import serializers
from .models import Booking
from django.utils import timezone

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        start = data['start']
        end = data['end']
        field_id = data['field_id']
        if start >= end:
            raise serializers.ValidationError('La fecha de inicio debe ser anterior al fin')

        overlapping = Booking.objects.filter(field_id=field_id, status='active').filter(
            start__lt=end, end__gt=start
        )
        if self.instance:
            overlapping = overlapping.exclude(id=self.instance.id)
        if overlapping.exists():
            raise serializers.ValidationError('Ya existe una reserva en ese rango horario')
        return data
