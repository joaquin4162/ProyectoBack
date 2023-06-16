# Create your views here.
#from django.shortcuts import render
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q
from .models import ProfesionalServicio
from django.views.generic import ListView
from apps.profesional.models import Profesional
from apps.servicio.models import Servicio
from django.shortcuts import redirect, render
from .forms import VincularServicioForm
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib import messages


# class ServicioProfesionalListView(ListView):
#     template_name = 'lista_servicios_profesionales.html'
#     context_object_name = 'profesional_servicios'

#     def get_queryset(self):
#         profesional_id = self.kwargs['profesional_id']
#         return ProfesionalServicio.objects.filter(
#             Q(profesional_id=profesional_id)& Q(servicio__is_deleted=False)
#         )

from django.urls import reverse_lazy

class ServicioProfesionalListView(ListView):
    template_name = 'lista_servicios_profesionales.html'
    context_object_name = 'profesional_servicios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profesional_id = self.kwargs['profesional_id']
        profesional = Profesional.objects.get(id=profesional_id)
        context['profesional'] = profesional
        context['vincular_url'] = reverse_lazy('profesionalservicio:vincular_servicio', kwargs={'profesional_id': profesional_id})
        return context

    def get_queryset(self):
        profesional_id = self.kwargs['profesional_id']
        return ProfesionalServicio.objects.filter(
            Q(profesional_id=profesional_id) & Q(servicio__is_deleted=False)
        )





# class VincularServicioView(ListView):
#     model = Servicio
#     template_name = 'vincular_servicio.html'
#     context_object_name = 'servicios_activos'
#     form_class = VincularServicioForm

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         profesional_id = self.kwargs['profesional_id']
#         profesional = Profesional.objects.get(id=profesional_id)
#         context['profesional'] = profesional
#         return context

#     def get_queryset(self):
#         return Servicio.objects.filter(is_deleted=False)

#     def post(self, request, *args, **kwargs):
#         profesional_id = self.kwargs['profesional_id']
#         profesional = Profesional.objects.get(id=profesional_id)
#         form = self.form_class(request.POST)

#         if form.is_valid():
#             servicio = form.cleaned_data['servicio']
#             ProfesionalServicio.objects.create(profesional=profesional, servicio=servicio)
#             return redirect('profesionalservicio:lista_servicios_profesionales', profesional_id=profesional_id)

#         return self.render_to_response(self.get_context_data(form=form))




class VincularServicioView(FormView):
    template_name = 'vincular_servicio.html'
    form_class = VincularServicioForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profesional_id = self.kwargs['profesional_id']
        profesional = Profesional.objects.get(id=profesional_id)
        context['profesional'] = profesional
        return context

    def form_valid(self, form):
        profesional_id = self.kwargs['profesional_id']
        profesional = Profesional.objects.get(id=profesional_id)
        servicio = form.cleaned_data['servicio']

        # Verificar si el servicio ya está vinculado al profesional
        if ProfesionalServicio.objects.filter(profesional=profesional, servicio=servicio).exists():
            messages.error(self.request, 'Este servicio ya está vinculado al profesional.')
            return redirect('profesionalservicio:vincular_servicio', profesional_id=profesional_id)

        # Crear el objeto ProfesionalServicio
        ProfesionalServicio.objects.create(profesional=profesional, servicio=servicio)
        return redirect('profesionalservicio:lista_servicios_profesionales', profesional_id=profesional_id)
