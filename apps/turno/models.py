from django.db import models
from datetime import date, timedelta
from apps.servicio.models import Servicio
from apps.profesionalservicio.models import ProfesionalServicio
# Create your models here.


class Fecha(models.Model):
    fecha = models.DateField()
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    @classmethod
    def generar_fechas_mes_corriente(cls):
        today = date.today()
        first_day = today.replace(day=1)
        next_month = (first_day + timedelta(days=32)).replace(day=1)
        servicios = Servicio.objects.all()  # Obtener todos los servicios disponibles

        fechas = []
        for servicio in servicios:
            current_day = first_day
            while current_day < next_month:
                fechas.append(cls(fecha=current_day, servicio=servicio))
                current_day += timedelta(days=1)

        cls.objects.bulk_create(fechas)




class Horario(models.Model):
    horario = models.TimeField()


class Turno(models.Model):
    profesional_servicio = models.ForeignKey(ProfesionalServicio, on_delete= models.CASCADE)
    fecha = models.ForeignKey(Fecha, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)