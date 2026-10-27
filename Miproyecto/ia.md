# Bitácora de Uso de Inteligencia Artificial (ia.md)

## 1. Herramienta utilizada y propósito
Se utilizó **Gemini (Google AI)** como asistente técnico para la formulación del plan del proyecto (`plan.md`), la estructuración inicial de la lógica de evaluación en `solucion.py` y la integración con la vista de Django.

## 2. Consulta concreta realizada
> "Tengo un problema de negocio para un albergue de adopción de mascotas que evalúa edad, metros de patio y cupos disponibles. Ayúdame a generar el código en Python para validar las reglas y mostrar un formulario en Django."

## 3. Qué estaba mal o sobraba en la respuesta, y cómo se corrigió
* **Problema detectado:** Inicialmente, el modelo generó un formulario donde el usuario debía ingresar manualmente la cantidad de cupos disponibles de mascotas por postulación. En la realidad de un albergue, el usuario adoptante no define el stock de animales disponibles.
* **Corrección aplicada:** Se modificó la lógica para que los cupos sean un valor interno del sistema (`CUPOS_TOTALES`). Se implementó la función `calcular_cupos_disponibles()` para que el sistema descuente dinámicamente los cupos disponibles leyendo cuántos registros con estado `"Aceptado"` existen en el archivo `datos.json`.
* **Ajuste de persistencia:** Se eliminaron las propuestas iniciales de modelos ORM/bases de datos relacionales para ceñirse estrictamente a la lectura y escritura mediante el módulo nativo `json` de Python[cite: 1].