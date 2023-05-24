# Create your views here.
from django.shortcuts import render
from .models import ProfesionalServicio

def lista_servicios_profesionales(request, profesional_id):
    profesional_servicios = ProfesionalServicio.objects.filter(profesional_id=profesional_id)
    context = {'profesional_servicios': profesional_servicios}
    return render(request, 'lista_servicios_profesionales.html', context)