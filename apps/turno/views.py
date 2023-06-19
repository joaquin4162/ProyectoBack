from django.shortcuts import render
from django.views import View
from .models import Fecha, Turno, Horario
from apps.profesionalservicio.models import ProfesionalServicio
from django.core.mail import send_mail, EmailMessage
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.accounts.models import CustomUser
from datetime import date

class GenerarFechasView(View):
    def get(self, request):
        if Fecha.objects.exists():
            fechas_generadas = True
        else:
            Fecha.generar_fechas_mes_corriente()
            fechas_generadas = True

        mensaje_exito = "Las fechas se han generado exitosamente."
        return render(request, 'exito.html', {'mensaje': mensaje_exito, 'fechas_generadas': fechas_generadas})
class SeleccionarFechaView(View):
    def get(self, request, servicio_id, profesionalservicio_id):
        profesionalservicio = ProfesionalServicio.objects.get(id=profesionalservicio_id)
        today = date.today()
        fechas = Fecha.objects.filter(servicio_id=servicio_id, fecha__gte=today)
        return render(request, 'seleccionar_fecha.html', {'fechas': fechas, 'servicio_id': servicio_id, 'profesionalservicio': profesionalservicio})

class SeleccionarHorarioView(View):
    def get(self, request, fecha_id, profesionalservicio_id):
        fecha = Fecha.objects.get(id=fecha_id)
        horarios_ocupados_fecha = Turno.objects.filter(fecha=fecha).values('horario')
        horarios_disponibles = Horario.objects.exclude(id__in=horarios_ocupados_fecha)
        profesionalservicio = ProfesionalServicio.objects.get(id=profesionalservicio_id)
        return render(request, 'seleccionar_horario.html', {'fecha': fecha, 'horarios': horarios_disponibles, 'profesionalservicio': profesionalservicio})


class ConfirmarTurnoView(View):
    def get(self, request, fecha_id, horario_id, profesionalservicio_id):
        fecha = Fecha.objects.get(id=fecha_id)
        horario = Horario.objects.get(id=horario_id)
        profesionalservicio = ProfesionalServicio.objects.get(id=profesionalservicio_id)
        return render(request, 'confirmar_turno.html', {'fecha': fecha, 'horario': horario, 'profesionalservicio': profesionalservicio})

    def post(self, request, fecha_id, horario_id, profesionalservicio_id):
        fecha = Fecha.objects.get(id=fecha_id)
        horario = Horario.objects.get(id=horario_id)
        profesionalservicio = ProfesionalServicio.objects.get(id=profesionalservicio_id)

        # Renderizar el template de confirmación del turno con los datos del turno
        return render(request, 'confirmar_turno.html', {'fecha': fecha, 'horario': horario, 'profesionalservicio': profesionalservicio})
    


class TurnoConfirmadoView(View):
    @method_decorator(login_required(login_url='accounts:login'))
    def post(self, request):
        fecha_id = request.POST.get('fecha_id')
        horario_id = request.POST.get('horario_id')
        profesionalservicio_id = request.POST.get('profesionalservicio_id')

        # Obtener los objetos de turno confirmado
        fecha = Fecha.objects.get(id=fecha_id)
        horario = Horario.objects.get(id=horario_id)
        profesionalservicio = ProfesionalServicio.objects.get(id=profesionalservicio_id)

        # Guardar los datos del turno en la base de datos
        turno = Turno.objects.create(fecha=fecha, horario=horario, profesional_servicio=profesionalservicio)

       # Obtener el correo electrónico del usuario desde la sesión
        user_email = request.user.email
        print(user_email)
        # Enviar correo electrónico de confirmación al usuario
        subject = 'Confirmación de turno'
        message = f'Tu turno ha sido confirmado exitosamente.\n\n' \
                  f'Fecha: {fecha.fecha}\n' \
                  f'Horario: {horario.horario}\n' \
                  f'Profesional: {profesionalservicio.profesional.nombre}\n' \
                  f'Servicio: {profesionalservicio.servicio.nombre}\n'
        from_email = 'peluquerya2023@gmail.com'
        to_email = [user_email]
         # Crear una instancia de EmailMessage y enviar el correo electrónico
        email = EmailMessage(subject, message, from_email, to_email)
        email.send()

        # Enviar una copia del correo electrónico al remitente
        copy_subject = 'Confirmación de turno - Copia'
        copy_message = f'Tu turno ha sido confirmado exitosamente.\n\n' \
                       f'Fecha: {fecha.fecha}\n' \
                       f'Horario: {horario.horario}\n' \
                       f'Profesional: {profesionalservicio.profesional.nombre}\n' \
                       f'Servicio: {profesionalservicio.servicio.nombre}\n' \
                       f'Correo electrónico del usuario: {user_email}\n'

        copy_email = EmailMessage(copy_subject, copy_message, from_email, ['peluquerya2023@gmail.com'])
        copy_email.send()    

        

        # Renderizar el template de turno confirmado con los datos del turno
        return render(request, 'turno_confirmado.html', {'turno': turno})
