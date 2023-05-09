from django.db import models
from apps.servicio.models import Servicio

# Create your models here.

class Profesional(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def nombre_servicio(self):
        return self.servicio.nombre