from django.db import models
from datetime import date, timedelta

# Create your models here.


class Fecha(models.Model):
    fecha = models.DateField()

    @classmethod
    def generar_fechas_mes_corriente(cls):
        today = date.today()
        first_day = today.replace(day=1)
        next_month = (first_day + timedelta(days=32)).replace(day=1)
        fechas = []
        current_day = first_day
        while current_day < next_month:
            fechas.append(cls(fecha=current_day))
            current_day += timedelta(days=1)
        cls.objects.bulk_create(fechas)


class Horario(models.Model):
    horario = models.TimeField()


class Turno(models.Model):
    profesional = models.ForeignKey('profesional.Profesional', on_delete=models.CASCADE)
    servicio = models.ForeignKey('profesionalservicio.ProfesionalServicio', on_delete=models.CASCADE)
    fecha = models.ForeignKey(Fecha, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)