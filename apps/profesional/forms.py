from django import forms
from .models import Profesional

class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = ['nombre', 'apellido', 'email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'ejemplo@ejemplo.com.ar'}),
        }
