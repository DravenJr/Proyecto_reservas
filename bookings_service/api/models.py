
from django.db import models

class Booking(models.Model):
    user_id = models.IntegerField()
    field_id = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    status = models.CharField(max_length=20, default='active')

    class Meta:
        indexes = [
            models.Index(fields=['field_id','start','end']),
        ]

    def __str__(self):
        return f"Booking {self.id} - field {self.field_id} - {self.start}"
