from django.urls import path
from .views import ProfesionalesListView, ProfesionalCreateView, ProfesionalDeleteView, ProfesionalesActivarView, ProfesionalesBorradosView

app_name = 'profesional'

urlpatterns= [
    path('lista/', ProfesionalesListView.as_view(), name = 'lista_profesionales'),

    path('crear/', ProfesionalCreateView.as_view(), name='crear_profesional'),

    path('borrar/<int:pk>/', ProfesionalDeleteView.as_view(), name='borrar_profesional'),

    path('activar/<int:pk>/', ProfesionalesActivarView.as_view(), name='activar_profesional'),

    path('borrados/', ProfesionalesBorradosView.as_view(), name='profesionales_borrados'),

]