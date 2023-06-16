from django.urls import path
from .views import ServicioProfesionalListView, VincularServicioView

app_name = 'profesionalservicio'

urlpatterns = [
    path('servicios_profesional/<int:profesional_id>/', ServicioProfesionalListView.as_view(), name='lista_servicios_profesionales'),

    path('vincular_servicio/<int:profesional_id>/', VincularServicioView.as_view(), name='vincular_servicio'),
    
    ]