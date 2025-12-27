import flet as ft
from ui.components.nav_bar import BarraNavegacion

class TareasScreen(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/Tareas",
            navigation_bar=BarraNavegacion(page),
            padding=20,
            bgcolor="#F5F5F5"
        )
        self.page = page

