from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Usuario(AbstractUser):
    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class Auditoria(models.Model):
    # Fecha
    creado = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha de creación",
        verbose_name="Creado a las",
        null=False,
        blank=False,
    )
    actualizado = models.DateTimeField(
        auto_now=True,
        verbose_name="Actualizado a las",
        help_text="Fecha de actualización",
        null=False,
        blank=False,
    )
    # Usuario
    creado_por = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        related_name="%(class)s_creado_por",
        null=False,
        blank=False,
        verbose_name="Creado por",
        help_text="Usuario que creó el registro",
    )
    actualizado_por = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        related_name="%(class)s_actualizado_por",
        null=False,
        blank=False,
        verbose_name="Actualizado por",
        help_text="Usuario que actualizó el registro",
    )
    # Otros campos
    activo = models.BooleanField(
        default=True,
        verbose_name="Activo",
        help_text="Estado del registro",
        null=False,
        blank=False,
        db_index=True,
    )

    class Meta:
        abstract = True
        ordering = ["-creado"]
