from django.db import models
from apps.servicio.models import Servicio

# Create your models here.

class Profesional(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)
