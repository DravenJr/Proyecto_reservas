
from django.db import models

class Field(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    capacity = models.IntegerField(default=10)
    price_per_hour = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
