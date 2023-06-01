from django.views.generic import ListView
from .models import Profesional


# Create your views here.

class ProfesionalesListView(ListView):
    template_name = 'lista_profesionales.html'
    context_object_name = 'profesionales'
    queryset = Profesional.objects.all()