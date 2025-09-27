
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Permission(models.Model):
    code = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.code

class UserRole(models.Model):
    user_id = models.IntegerField()  # id del usuario en auth_service
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
