from django.urls import path
from .views import SeleccionarFechaView, SeleccionarHorarioView, ConfirmarTurnoView

app_name = 'turno'

urlpatterns = [
    path('seleccionar_fecha/', SeleccionarFechaView.as_view(), name='seleccionar_fecha'),
    path('seleccionar_horario/<int:fecha_id>/', SeleccionarHorarioView.as_view(), name='seleccionar_horario'),
    path('confirmar_turno/', ConfirmarTurnoView.as_view(), name= 'confirmar_turno'),
]