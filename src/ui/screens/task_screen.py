import flet as ft
from ui.components.nav_bar import BarraNavegacion

class TareasScreen(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/Tareas",
            navigation_bar=BarraNavegacion(page),
            padding=20,
            bgcolor="#F5F5F5",
            # ¡FALTABA ESTO! Sin controles, la vista es inválida
            controls=[
                ft.AppBar(title=ft.Text("Mis Tareas"), bgcolor=ft.Colors.RED),
                ft.Text("Aquí aparecerán tus tareas", size=20)
            ]
        )
        self.page = page

