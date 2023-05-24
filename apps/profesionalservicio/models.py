from django.db import models
from apps.profesional.models import Profesional
from apps.servicio.models import Servicio

# Create your models here.

class ProfesionalServicio(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete = models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha_borrado = models.DateField(null= True)
    # Otros campos o métodos relacionados a la relación Profesional-Servicio
