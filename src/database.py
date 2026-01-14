tareas_globales = []

nueva_tarea = {
        "nombre": 'Comprar',
        "fecha": '23-jun-26',
        "prioridad": 'Alta',
        "completada": False
    }

tareas_globales.append(nueva_tarea)

def get(key):
    if key == "mis_tareas":
        return tareas_globales
    return None

def set(key, value):
    if key == "mis_tareas":
        tareas_globales.clear()
        tareas_globales.extend(list(value))