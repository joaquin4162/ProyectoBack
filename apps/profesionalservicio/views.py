# Create your views here.
#from django.shortcuts import render
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q
from .models import ProfesionalServicio
from django.views.generic import ListView
from apps.profesional.models import Profesional

# def lista_servicios_profesionales(request, profesional_id):
#     profesional_servicios = ProfesionalServicio.objects.filter(profesional_id=profesional_id)
#     context = {'profesional_servicios': profesional_servicios}
#     return render(request, 'lista_servicios_profesionales.html', context)


class ServicioProfesionalListView(ListView):
    template_name = 'lista_servicios_profesionales.html'
    context_object_name = 'profesional_servicios'

    def get_queryset(self):
        profesional_id = self.kwargs['profesional_id']
        return ProfesionalServicio.objects.filter(
            Q(profesional_id=profesional_id)& Q(servicio__is_deleted=False)
        )