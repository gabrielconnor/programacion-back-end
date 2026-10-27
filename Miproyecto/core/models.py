from django.db import models
from django.utils import timezone

class SolicitudAdopcion(models.Model):
    ESTADO_CHOICES = [
        ("Aceptado", "Aceptado"),
        ("Rechazado", "Rechazado"),
        ("Dato Inválido", "Dato Inválido"),
    ]

    nombre = models.CharField(max_length=120)
    edad = models.IntegerField()
    metros_patio = models.FloatField()
    cupos_al_momento = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    motivo = models.CharField(max_length=255)
    fecha = models.DateTimeField(default=timezone.now)

    # Borrado lógico (no se destruye la fila, solo se oculta)
    eliminado = models.BooleanField(default=False)
    fecha_eliminacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-fecha"]
        verbose_name = "Solicitud de Adopción"
        verbose_name_plural = "Solicitudes de Adopción"

    def __str__(self):
        return f"{self.nombre} - {self.estado} ({self.fecha.strftime('%d/%m/%Y')})"

    def soft_delete(self):
        self.eliminado = True
        self.fecha_eliminacion = timezone.now()
        self.save()