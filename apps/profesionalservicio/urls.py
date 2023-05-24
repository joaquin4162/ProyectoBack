from django.urls import path
from . import views

app_name = 'profesionalservicio'

urlpatterns = [
    path('servicios_profesional/<int:profesional_id>/', views.lista_servicios_profesionales, name='lista_servicios_profesionales'),
]