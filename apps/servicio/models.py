from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.FloatField()
    is_deleted = models.BooleanField(default=False)


    def __str__(self):
        return self.nombre
    


# agregar agenta y usuario como aplicacion
# agenda se va a vincular a los turnos, los turnos se tienen que chekear una agenda, y esta agenda le va a pertenecer
#a un profesional