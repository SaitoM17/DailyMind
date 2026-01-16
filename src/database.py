tareas_globales = []
categorias_globales = []

nueva_tarea = {
        "nombre": 'Comprar',
        'categoria': 'Escuela',
        "fecha": '23-jun-26',
        "prioridad": 'Alta',
        "completada": False
    }

categoria1 = {
    'categoria': 'Escuela'
}

categoria2 = {
    'categoria': 'Trabajo'
}

categoria3 = {
    'categoria': 'Hogar'
}

categoria4 = {
    'categoria': 'Mascota'
}

categoria5 = {
    'categoria': 'Jardín'
}

categoria6 = {
    'categoria': 'Texto largo para ver el como se muestra en pantalla'
}

categoria7 = {
    'categoria': 'Texto largo para ver el como se muestra'
}

tareas_globales.append(nueva_tarea)

categorias_globales.append(categoria1)
categorias_globales.append(categoria2)
categorias_globales.append(categoria3)
categorias_globales.append(categoria4)
categorias_globales.append(categoria5)
categorias_globales.append(categoria6)
categorias_globales.append(categoria7)

def get(key):
    if key == "mis_tareas":
        return tareas_globales
    return None

def set(key, value):
    if key == "mis_tareas":
        tareas_globales.clear()
        tareas_globales.extend(list(value))

def get_categoria(key):
    if key == 'mis_categorias':
        return categorias_globales
    return None