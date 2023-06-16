from django import forms
from apps.servicio.models import Servicio

class VincularServicioForm(forms.Form):
    servicio = forms.ModelChoiceField(queryset=Servicio.objects.filter(is_deleted=False))
