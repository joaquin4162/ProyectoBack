from django.urls import path
from .views import LoginView, LogoutView, Registerview

app_name = 'usuario'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', Registerview.as_view(), name='register'),

]