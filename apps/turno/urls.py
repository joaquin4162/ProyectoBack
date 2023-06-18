from django.urls import path
from .views import SeleccionarFechaView, SeleccionarHorarioView, ConfirmarTurnoView, TurnoConfirmadoView, GenerarFechasView

app_name = 'turno'

urlpatterns = [
    path('seleccionar_fecha/<int:servicio_id>/<int:profesionalservicio_id>/', SeleccionarFechaView.as_view(), name='seleccionar_fecha'),
    path('seleccionar_horario/<int:fecha_id>/<int:profesionalservicio_id>/', SeleccionarHorarioView.as_view(), name='seleccionar_horario'),
    path('confirmar_turno/<int:fecha_id>/<int:horario_id>/<int:profesionalservicio_id>/', ConfirmarTurnoView.as_view(), name='confirmar_turno'),
    path('turno_confirmado/', TurnoConfirmadoView.as_view(), name='turno_confirmado'),
    path('generar_fechas/', GenerarFechasView.as_view(), name='generar_fechas'),
]
