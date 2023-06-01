from django.urls import path
from .views import ProfesionalesListView

app_name = 'profesional'

urlpatterns= [
    path('lista/', ProfesionalesListView.as_view(), name = 'lista_profesionales'),

]