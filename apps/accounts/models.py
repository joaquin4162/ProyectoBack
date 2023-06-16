from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Utilizar el campo email como identificador único
    USERNAME_FIELD = 'email'  # Establecer el campo email como el campo de autenticación
    REQUIRED_FIELDS = []  # No se requieren campos adicionales para la creación de usuario

    def __str__(self):
        return self.email
