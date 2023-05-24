from django.contrib import admin
from apps.profesionalservicio.models import ProfesionalServicio
# Register your models here.

class ProfesionalServicioAdmin(admin.ModelAdmin):
    list_display = ('profesional', 'servicio', 'fecha_borrado')

admin.site.register(ProfesionalServicio, ProfesionalServicioAdmin)

