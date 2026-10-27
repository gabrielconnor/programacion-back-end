# Sistema de Gestión y Evaluación de Adopciones - Albergue de Mascotas

Backend desarrollado con **Django** y **SQLite** para la gestión y evaluación automatizada de solicitudes de adopción de mascotas, garantizando la persistencia de datos relacionales, control de acceso por roles y borrado lógico.

---

## 📋 Características Principales

1. **Persistencia en Base de Datos Relacional:** Migración completa desde archivos planos (`datos.json`) hacia base de datos SQLite administrada mediante modelos ORM de Django.
2. **Cálculo de Disponibilidad en Tiempo Real:** Control dinámico de capacidad del albergue (cupos totales vs. cupos disponibles calculados según adopciones aceptadas).
3. **Reglas de Negocio Automatizadas:** Evaluación del estado de la postulación (`Aceptado`, `Rechazado`, `Dato Inválido`) con motivo detallado.
4. **Control de Acceso y Roles:** Autenticación de usuarios con permisos diferenciados (Administrador vs. Usuario Estándar/Voluntario).
5. **Borrado Lógico (*Soft Delete*):** Los registros eliminados no se destruyen físicamente en la base de datos, sino que se marcan como inactivos mediante una bandera booleana (`eliminado=True`).

---

## ⚙️ Reglas de Negocio del Sistema

La evaluación de cada solicitud se realiza según las siguientes condiciones:
* **Dato Inválido:** Si la edad es menor a 0 o mayor a 120, o si los metros de patio o cupos son números negativos.
* **Rechazado (Edad):** Si el postulante es menor de 18 años.
* **Rechazado (Espacio):** Si el patio disponible es menor a 15 m².
* **Rechazado (Capacidad):** Si el albergue no cuenta con cupos disponibles al momento de la postulación.
* **Aceptado:** Si cumple con la mayoría de edad, el espacio mínimo de patio y existen cupos disponibles.

---

## 🚀 Instalación y Puesta en Marcha

### 1. Clonar o descargar el repositorio
Ubícate en la carpeta raíz del proyecto donde se encuentra `manage.py`.

### 2. Crear y activar el entorno virtual
En Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1