from django.shortcuts import render
from .models import Servicio


# Create your views here.


def lista_servicios(request):
    servicios = Servicio.objects.filter(is_deleted=False)
    context = {'servicios': servicios}
    return render(request, 'Servicios.html', context)