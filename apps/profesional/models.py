from django.db import models
from apps.servicio.models import Servicio

# Create your models here.

class Profesional(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField(blank=False, null=False)
    is_deleted = models.BooleanField(default=False)


    def delete(self):
        self.is_deleted = True
        self.save()


