import flet as ft

def CrearEditarEliminarHabitoScreen(page: ft.Page):
    task_input = ft.TextField(label="¿Qué hay que hacer?", autofocus=True)
    
    def guardar_tarea(e):
        print(f"Hábito guardada: {task_input.value}")
        page.go("/") # Regresa al inicio tras guardar

    return ft.View(
        "/create",
        controls=[
            ft.AppBar(title=ft.Text("Crear Nuevo Hábito"), bgcolor=ft.Colors.AMBER),
            ft.SafeArea(
                content=ft.Column([
                    ft.Text("Detalles del Hábito", size=20, weight="bold"),
                    task_input,
                    ft.ElevatedButton("Guardar Hábito", on_click=guardar_tarea)
                ], spacing=20)
            )
        ]
    )