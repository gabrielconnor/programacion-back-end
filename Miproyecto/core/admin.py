from django.contrib import admin
from .models import SolicitudAdopcion

@admin.register(SolicitudAdopcion)
class SolicitudAdopcionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "edad", "metros_patio", "estado", "fecha", "eliminado")
    list_filter = ("estado", "eliminado", "fecha")
    search_fields = ("nombre", "motivo")
    readonly_fields = ("fecha_eliminacion",)