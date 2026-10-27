"""
URL configuration for Miproyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Ruta principal conectada a lista_solicitudes
    path('', views.lista_solicitudes, name='lista_solicitudes'),
    
    # Gestión de solicitudes
    path('solicitudes/crear/', views.crear_solicitud, name='crear_solicitud'),
    path('solicitudes/<int:pk>/editar/', views.editar_solicitud, name='editar_solicitud'),
    path('solicitudes/<int:pk>/eliminar/', views.eliminar_solicitud, name='eliminar_solicitud'),
    
    # Autenticación estándar de Django
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]