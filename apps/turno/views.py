
from django.shortcuts import render, redirect
from django.views import View
from .models import Fecha, Turno,Horario
from apps.profesional.models import Profesional
from apps.profesionalservicio.models import ProfesionalServicio

class SeleccionarFechaView(View):
    def get(self, request):
        fechas = Fecha.objects.all()
        return render(request, 'seleccionar_fecha.html', {'fechas': fechas})

# class SeleccionarHorarioView(View):
#     def get(self, request, fecha_id):
#         fecha = Fecha.objects.get(id=fecha_id)
#         profesional_id = request.session.get('profesional_id')
#         servicios_vinculados = ProfesionalServicio.objects.filter(profesional_id=profesional_id)
#         horarios_disponibles = Horario.objects.exclude(turno__fecha=fecha, turno__profesional__id=profesional_id).distinct()
#         print(horarios_disponibles)
#         return render(request, 'seleccionar_horario.html', {'fecha': fecha, 'horarios': horarios_disponibles})
    
class SeleccionarHorarioView(View):
    def get(self, request, fecha_id):
        fecha = Fecha.objects.get(id=fecha_id)
        profesional_id = request.session.get('profesional_id')

        # Excluir los horarios ocupados por fecha
        horarios_ocupados_fecha = Turno.objects.filter(fecha=fecha).values('horario')
        horarios_disponibles = Horario.objects.exclude(id__in=horarios_ocupados_fecha)

        # Excluir los horarios ocupados por el profesional
        horarios_ocupados_profesional = Turno.objects.filter(profesional_id=profesional_id).values('horario')
        horarios_disponibles = horarios_disponibles.exclude(id__in=horarios_ocupados_profesional)

        return render(request, 'seleccionar_horario.html', {'fecha': fecha, 'horarios': horarios_disponibles})    

    def post(self, request, fecha_id):
        horario_id = request.POST.get('horario_id')
        fecha = Fecha.objects.get(id=fecha_id)
        profesional_id = request.session.get('profesional_id')
        # Aquí debes guardar el turno con el horario seleccionado
        return redirect('turno:confirmar_turno')


class ConfirmarTurnoView(View):
    def get(self, request):
        return render(request, 'confirmar_turno.html')