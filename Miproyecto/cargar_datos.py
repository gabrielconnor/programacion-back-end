import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Miproyecto.settings")
django.setup()

from core.models import SolicitudAdopcion

def migrar():
    if not os.path.exists("datos.json"):
        print("Error: No se encontro datos.json")
        return

    with open("datos.json", "r", encoding="utf-8") as f:
        try:
            datos = json.load(f)
        except json.JSONDecodeError:
            print("datos.json esta vacio o corrupto.")
            return

    lista = datos if isinstance(datos, list) else datos.get("registros", [])

    for item in lista:
        SolicitudAdopcion.objects.create(
            nombre=item.get("nombre", "Sin nombre"),
            edad=item.get("edad", 0),
            metros_patio=item.get("metros_patio", item.get("espacio", 0.0)),
            cupos_al_momento=item.get("cupos", item.get("cupos_mascotas", 0)),
            estado=item.get("estado", "Evaluado"),
            motivo=item.get("motivo", "")
        )

    print(f"Exito: Se migraron {len(lista)} registros desde datos.json a db.sqlite3.")

if __name__ == "__main__":
    migrar()
