from django.shortcuts import render
from .models import Profesional


# Create your views here.


def lista_profesionales(request):
    profesionales = Profesional.objects.all()
    context = {'profesionales': profesionales}
    return render(request,'lista_profesionales.html', context)