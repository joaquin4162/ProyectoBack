from django.urls import path
from .views import ServicioProfesionalListView

app_name = 'profesionalservicio'

urlpatterns = [
    path('servicios_profesional/<int:profesional_id>/', ServicioProfesionalListView.as_view(), name='lista_servicios_profesionales'),
]