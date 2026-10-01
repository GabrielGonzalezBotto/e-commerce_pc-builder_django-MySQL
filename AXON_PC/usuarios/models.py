from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")
    postal = models.CharField(max_length=10, blank=True, null=True, verbose_name="Código Postal")
    direccion = models.CharField(max_length=255, blank=True, null=True, verbose_name="Dirección de Envío")
    
    groups = models.ManyToManyField(
        Group,
        related_name='usuario_set',
        blank=True,
        help_text='Grupos a los que pertence este usuario.',
        verbose_name='grupos',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuarios_user_set',
        blank=True,
        help_text='Permisos específicos para este usuario.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username