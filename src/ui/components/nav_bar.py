import flet as ft

class BarraNavegacion(ft.NavigationBar):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        # CAMBIO AQUÍ: NavigationBarDestination
        self.destinations = [
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Incio"),
            ft.NavigationBarDestination(icon=ft.Icons.TASK, label="Tareas"),
            ft.NavigationBarDestination(icon=ft.Icons.TRACK_CHANGES,label="Hábitos"),
            ft.NavigationBarDestination(icon=ft.Icons.ANALYTICS, label='Estadística')
        ]
        self.selected_index = 0 if page.route == "/" else 1
        self.on_change = self.cambiar_ruta

    def cambiar_ruta(self, e):
        if e.control.selected_index == 0:
            self.page.go("/")
        elif e.control.selected_index == 1:
            self.page.go("/Tareas")