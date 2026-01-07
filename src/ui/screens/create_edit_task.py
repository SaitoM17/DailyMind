import flet as ft

def CrearEditarEliminarTareaScreen(page: ft.Page):
    # Campos de texto para la tarea
    task_input = ft.TextField(label="¿Qué hay que hacer?", autofocus=True)
    
    def guardar_tarea(e):
        print(f"Tarea guardada: {task_input.value}")
        page.go("/") # Regresa al inicio tras guardar

    return ft.View(
        "/create",
        controls=[
            ft.AppBar(title=ft.Text("Crear Nueva Tarea"), bgcolor=ft.Colors.AMBER),
            ft.SafeArea(
                content=ft.Column([
                    ft.Text("Detalles de la tarea", size=20, weight="bold"),
                    task_input,
                    ft.ElevatedButton("Guardar Tarea", on_click=guardar_tarea)
                ], spacing=20)
            )
        ]
    )