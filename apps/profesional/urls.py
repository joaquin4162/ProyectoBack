from django.urls import path
from .views import lista_profesionales

urlpatterns= [
    path('lista/', lista_profesionales, name = 'lista_profesionales'),

]