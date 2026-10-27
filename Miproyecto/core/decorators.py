# tu_app/decorators.py
from django.core.exceptions import PermissionDenied
from functools import wraps

def role_required(allowed_roles=[]):
    """
    Verifica que el usuario pertenezca a al menos uno de los roles permitidos,
    o que sea superusuario. Si no cumple, lanza un error HTTP 403 (Forbidden).
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                from django.contrib.auth.views import redirect_to_login
                return redirect_to_login(request.get_full_path())
            
            # Superusuarios siempre tienen acceso total
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)

            # Verificar si el usuario está en alguno de los grupos permitidos
            user_groups = request.user.groups.values_list('name', flat=True)
            if any(rol in user_groups for rol in allowed_roles):
                return view_func(request, *args, **kwargs)

            # Si no pertenece a ningún grupo autorizado, rechazar con 403
            raise PermissionDenied
        return _wrapped_view
    return decorator