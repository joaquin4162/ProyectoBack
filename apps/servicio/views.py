from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import DeleteView, ListView
from django.urls import reverse_lazy
from .forms import ServicioForm
from .models import Servicio
from apps.profesionalservicio.models import ProfesionalServicio

# Create your views here.


# def lista_servicios(request):
#     servicios = Servicio.objects.filter(is_deleted=False)
#     context = {'servicios': servicios}
#     return render(request, 'Servicios.html', context)


class ListaServiciosView(View):
    def get(self, request):
        servicios = Servicio.objects.filter(is_deleted=False)
        context = {'servicios':servicios}
        return render(request, 'Servicios.html', context)
    

class CrearServicioView(View):
    def get(self, request):
        form = ServicioForm()
        context = {'form':form}
        return render(request, 'crear_servicio.html', context)
    
    def post(self, request):
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicio:lista_servicios')
        context = {'form': form}
        return render(request, 'crear_servicio.html', context)
    




class ServicioDeleteView(DeleteView):
    def post(self, request, pk):
        servicio = Servicio.objects.get(pk=pk)
        servicio.delete()
        return redirect('servicio:lista_servicios')


class ServicioBorradosView(ListView):
    model = Servicio
    template_name = 'servicios_borrados.html'
    context_object_name = 'servicios'

    def get_queryset(self):
        return Servicio.objects.filter(is_deleted=True)
    
class ServicioActivarView(View):
    def post(self, request, pk):
        servicio = Servicio.objects.get(pk=pk)
        servicio.is_deleted = False
        servicio.save()
        return redirect('servicio:lista_servicios')
    

class ProfesionalesDisponiblesView(View):
    template_name = 'profesional_disponibles.html'

    def get(self, request, servicio_id):
        servicio = Servicio.objects.get(pk=servicio_id)
        profesionales_disponibles = servicio.profesionalservicio_set.all()
        context = {
            'servicio': servicio,
            'profesionales_disponibles': profesionales_disponibles
        }
        return render(request, self.template_name, context)