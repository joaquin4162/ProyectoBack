from django.contrib import admin
from apps.servicio.models import Servicio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')

admin.site.register(Servicio, ServicioAdmin)