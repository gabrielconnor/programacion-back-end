from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .decorators import role_required
from .models import SolicitudAdopcion
from .forms import SolicitudAdopcionForm  # Asegúrate de que este sea el nombre de tu formulario


# 1. LISTADO (admin, normal, viewer)
@login_required
@role_required(allowed_roles=['admin', 'normal', 'viewer'])
def lista_solicitudes(request):
    # Filtrar solo las solicitudes no eliminadas
    solicitudes = SolicitudAdopcion.objects.filter(eliminado=False)
    return render(request, 'solicitudes/lista.html', {'solicitudes': solicitudes})


# 2. CREAR (admin, normal)
@login_required
@role_required(allowed_roles=['admin', 'normal'])
def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudAdopcionForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            
            # Si tienes función de evaluación de reglas, aplícala aquí:
            # estado, motivo = evaluar_reglas(solicitud)
            # solicitud.estado = estado
            # solicitud.motivo = motivo
            
            solicitud.save()
            return redirect('lista_solicitudes')
    else:
        form = SolicitudAdopcionForm()
    return render(request, 'solicitudes/crear.html', {'form': form})


# 3. EDITAR (admin, normal)
@login_required
@role_required(allowed_roles=['admin', 'normal'])
def editar_solicitud(request, pk):
    solicitud = get_object_or_404(SolicitudAdopcion, pk=pk, eliminado=False)
    if request.method == 'POST':
        form = SolicitudAdopcionForm(request.POST, instance=solicitud)
        if form.is_valid():
            solicitud_actualizada = form.save(commit=False)
            
            # Re-evaluar reglas si se modificaron datos clave:
            # estado, motivo = evaluar_reglas(solicitud_actualizada)
            # solicitud_actualizada.estado = estado
            # solicitud_actualizada.motivo = motivo
            
            solicitud_actualizada.save()
            return redirect('lista_solicitudes')
    else:
        form = SolicitudAdopcionForm(instance=solicitud)
    return render(request, 'solicitudes/editar.html', {'form': form, 'solicitud': solicitud})


# 4. ELIMINAR (Solo admin)
@login_required
@role_required(allowed_roles=['admin'])
def eliminar_solicitud(request, pk):
    solicitud = get_object_or_404(SolicitudAdopcion, pk=pk, eliminado=False)
    if request.method == 'POST':
        # Borrado lógico (soft-delete) usando los campos reales de tu modelo
        solicitud.eliminado = True
        solicitud.fecha_eliminacion = timezone.now()
        solicitud.save()
        return redirect('lista_solicitudes')
    return render(request, 'solicitudes/confirmar_eliminar.html', {'solicitud': solicitud})