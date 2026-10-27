# Plan de Proyecto: Sistema de Evaluación de Adopciones

## 1. Apartado de Negocio

### Problema
Un albergue de mascotas recibe múltiples solicitudes de adopción semanalmente, pero no da abasto para evaluar de forma manual si cada postulante cumple con los requisitos mínimos de edad, espacio libre en su hogar y disponibilidad de animales. Esto retrasa las respuestas y genera inconsistencias en la evaluación.

### Solución
Un sistema backend ligero que automatiza la revisión de los criterios esenciales (edad, metros de patio y cupos), entregando un veredicto inmediato con su motivo correspondiente y registrando la información para control del albergue.

### Alcance
* **Dentro del alcance:** Validación de entradas, regla de negocio con 4 resultados, persistencia de datos y visualización del listado en una pantalla web en Django.
* **Fuera del alcance:** Pasarelas de pago, envío automatizado de correos electrónicos y geolocalización de hogares.

### Priorización MoSCoW
* **Must (MVP - Obligatorio):**
  * Validación de tipos de datos de entrada (`edad`, `metros_patio`, `cupos_mascotas`).
  * Regla de decisión con 4 resultados posibles usando condicionales `if/elif/else`.
  * Guardado de registros en `datos.json`.
  * Visualización web del historial mediante vista y plantilla en Django.
* **Should (Importante):**
  * Edición o corrección manual de datos mal ingresados.
* **Could (Deseable):**
  * Exportar el listado de adopciones a formato CSV.
* **Won't (Fuera por ahora):**
  * Roles diferenciados de usuario (administrador general vs. voluntario).

---

## 2. Apartado Técnico

### Datos de Entrada
* `edad` (entero): Edad del adoptante (mínimo responsable: 18 años).
* `metros_patio` (flotante/entero): Metros cuadrados disponibles de patio o espacio libre.
* `cupos_mascotas` (entero): Cantidad de mascotas disponibles para adopción.

### Regla de Decisión (4 Resultados)
1. **Dato Inválido:** Si `edad < 0` o `edad > 120`, o `metros_patio < 0`, o `cupos_mascotas < 0`.
2. **Aceptado:** Si `edad >= 18`, `metros_patio >= 15` y `cupos_mascotas > 0`.
3. **Rechazo 1 (Espacio insuficiente):** Si `edad >= 18` y `metros_patio < 15`.
4. **Rechazo 2 (Sin cupos disponibles):** Si `edad >= 18`, `metros_patio >= 15` y `cupos_mascotas == 0`.

### Paquete Externo
* **`tabulate`:** Empleado en `solucion.py` para dar formato de tabla por consola al historial de solicitudes.

### Pantalla Web
* **Ruta:** `/` (página principal).
* **Vista:** Lee la información persistida y entrega el contexto a la plantilla `resumen.html`.