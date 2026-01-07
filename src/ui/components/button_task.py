import flet as ft

class ButtonCrearTarea(ft.ElevatedButton):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.content=ft.Row(
            [
                ft.Text(value='Nueva Tarea', size=18),
                ft.Icon(name=ft.Icons.ADD)
            ],
            tight=True,
            spacing=10
        )
        self.on_click = self.nueva_tarea
        self.style=ft.ButtonStyle(
                color=ft.Colors.BLACK,
                bgcolor="#ffffff",
                shape=ft.RoundedRectangleBorder(radius=15),
            )

    def nueva_tarea(self, e):
        self.page.go("/create")