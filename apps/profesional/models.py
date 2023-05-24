from django.db import models
from apps.servicio.models import Servicio

# Create your models here.


#tenemos que modificar la fk, para crear una tabla intermedia
class Profesional(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    #servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    #def nombre_servicio(self):
    #    return self.servicio.nombre