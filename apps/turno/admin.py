from django.contrib import admin
from .models import Fecha, Turno, Horario


# Register your models here.


admin.site.register(Fecha)
admin.site.register(Horario)
admin.site.register(Turno)