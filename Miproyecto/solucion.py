import json
import os
from tabulate import tabulate

CUPOS_TOTALES = 50  # Capacidad máxima inicial del albergue

def calcular_cupos_disponibles(registros):
    """Calcula cuántos cupos quedan restando los aceptados previamente."""
    aceptados = sum(1 for r in registros if r.get("estado") == "Aceptado")
    return max(0, CUPOS_TOTALES - aceptados)

def evaluar_adopcion(nombre: str, edad: int, metros_patio: float, cupos_disponibles: int):
    """
    Evalúa la solicitud según las 4 reglas de negocio.
    """
    # 1. Caso dato inválido
    if edad < 0 or edad > 120 or metros_patio < 0:
        return "Dato Inválido", "Edad o medidas fuera de rango válido"
    
    # 2. Menor de edad
    elif edad < 18:
        return "Rechazado", "El solicitante debe ser mayor de edad (18 años o más)"
    
    # 3. Espacio insuficiente
    elif metros_patio < 15.0:
        return "Rechazado", "Espacio insuficiente (requiere al menos 15 m² de patio)"
    
    # 4. Sin cupos disponibles
    elif cupos_disponibles == 0:
        return "Rechazado", "No hay cupos disponibles de mascotas para adopción"
    
    # 5. Aceptado
    elif edad >= 18 and metros_patio >= 15.0 and cupos_disponibles > 0:
        return "Aceptado", "Cumple con todos los requisitos de adopción"
    
    else:
        return "Dato Inválido", "Condición no prevista"

def main():
    print("==============================================")
    print("   SISTEMA DE EVALUACIÓN DE ADOPCIONES        ")
    print("==============================================")
    
    # Cargar registros históricos previos
    archivo_json = "datos.json"
    registros = []
    if os.path.exists(archivo_json):
        try:
            with open(archivo_json, "r", encoding="utf-8") as f:
                registros = json.load(f)
        except (json.JSONDecodeError, ValueError):
            registros = []

    # Cálculo automático de cupos
    cupos_disponibles = calcular_cupos_disponibles(registros)
    print(f"Cupos actuales disponibles en el albergue: {cupos_disponibles}/{CUPOS_TOTALES}\n")

    nombre = input("Nombre del solicitante: ").strip()
    try:
        edad = int(input("Edad: "))
        metros_patio = float(input("Metros cuadrados de patio (m²): "))
    except ValueError:
        print("\n[ERROR] Entrada inválida: La edad y el metraje deben ser números.")
        return

    # Evaluación con cupos calculados internamente
    estado, motivo = evaluar_adopcion(nombre, edad, metros_patio, cupos_disponibles)
    
    print(f"\n--- Resultado para {nombre} ---")
    print(f"Estado: {estado}")
    print(f"Motivo: {motivo}")

    # Guardar nuevo registro
    nuevo_registro = {
        "nombre": nombre,
        "edad": edad,
        "metros_patio": metros_patio,
        "cupos_al_momento": cupos_disponibles,
        "estado": estado,
        "motivo": motivo
    }
    registros.append(nuevo_registro)

    with open(archivo_json, "w", encoding="utf-8") as f:
        json.dump(registros, f, indent=2, ensure_ascii=False)

    # Mostrar tabla actualizada
    print("\n--- Historial de Postulaciones (Tabulate) ---")
    print(tabulate(registros, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()