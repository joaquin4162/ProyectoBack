from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, View, DeleteView
from django.shortcuts import get_object_or_404, redirect
from .models import Profesional
from .forms import ProfesionalForm
from django.urls import reverse_lazy



# Create your views here.

class ProfesionalesListView(ListView):
    template_name = 'lista_profesionales.html'
    context_object_name = 'profesionales'
    queryset = Profesional.objects.all()

class ProfesionalCreateView(CreateView):
    model = Profesional
    form_class = ProfesionalForm 
    template_name = 'crear_profesional.html'
    success_url = reverse_lazy('profesional:lista_profesionales')


class ProfesionalDeleteView(DeleteView):
    def post(self, request, pk):
        profesional = Profesional.objects.get(pk=pk)
        profesional.delete()
        return redirect('profesional:lista_profesionales')




class ProfesionalesBorradosView(ListView):
    model = Profesional
    template_name = 'profesionales_borrados.html'
    context_object_name = 'profesionales'

    def get_queryset(self):
        return Profesional.objects.filter(is_deleted=True)
    
class ProfesionalesActivarView(View):
    def post(self, request, pk):
        profesional = Profesional.objects.get(pk=pk)
        profesional.is_deleted = False
        profesional.save()
        return redirect('profesional:lista_profesionales')