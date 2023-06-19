from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Utilizar el campo email como identificador único
    USERNAME_FIELD = 'email'  # Establecer el campo email como el campo de autenticación
    REQUIRED_FIELDS = []  # No se requieren campos adicionales para la creación de usuario

    def __str__(self):
        return self.email
GRUPO_USUARIO = 'usuarios'
@receiver(post_save, sender=CustomUser)
def asignar_permiso_usuario(sender, instance, created, **kwargs):
    if created:
        # Verificar si el grupo ya existe
        grupo_usuario, _ = Group.objects.get_or_create(name=GRUPO_USUARIO)
        # Asignar el grupo al usuario recién creado
        instance.groups.add(grupo_usuario)