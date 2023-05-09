from django.contrib import admin
from apps.profesional.models import Profesional

# Register your models here.

class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'nombre_servicio')


admin.site.register(Profesional, ProfesionalAdmin)