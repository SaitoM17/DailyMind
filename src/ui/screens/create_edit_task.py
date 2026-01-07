import flet as ft

def CrearEditarEliminarTareaScreen(page: ft.Page):
    
    appbar = ft.AppBar(
        leading=ft.IconButton(
            ft.Icons.CLEAR,
            icon_size=25, 
            on_click=lambda _:page.go('/')
            ),
            title=ft.Text('Crear Tarea'),
            center_title=True,
            bgcolor=ft.Colors.with_opacity(0.04, ft.CupertinoColors.SYSTEM_BACKGROUND),
    )

    # Campos de texto para la tarea
    task_input = ft.TextField(label="¿Qué hay que hacer?", autofocus=True)
    
    def guardar_tarea(e):
        print(f"Tarea guardada: {task_input.value}")
        page.go("/") # Regresa al inicio tras guardar

    return ft.View(
        "/create",
        controls=[
            appbar,
            ft.SafeArea(
                content=ft.Column([
                    ft.Text("Detalles de la tarea", size=20, weight="bold"),
                    task_input,
                    ft.ElevatedButton("Guardar Tarea", on_click=guardar_tarea)
                ], spacing=20)
            )
        ]
    )