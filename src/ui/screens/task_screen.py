import flet as ft

class TareasScreen(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/tareas",
            padding=20,
            bgcolor="#F5F5F5"
        )
        self.page = page

