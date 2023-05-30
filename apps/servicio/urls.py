from django.urls import path
from .views import ListaServiciosView, CrearServicioView, ServicioDeleteView, ServicioActivarView, ServicioBorradosView

urlpatterns= [
    path('lista/', ListaServiciosView.as_view(), name = 'lista_servicios'),
    path('crear/', CrearServicioView.as_view(), name='crear_servicio'),
    path('borrar/<int:pk>/', ServicioDeleteView.as_view(), name='borrar_servicio'),
    path('activar/<int:pk>/',ServicioActivarView.as_view(), name='activar_servicio' ),
    path('borrados/', ServicioBorradosView.as_view(), name='servicios_borrados'),
]



