import flet as ft

class BarraNavegacion(ft.NavigationBar):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        
        # Definimos las rutas en orden
        rutas = ['/', '/Tareas', '/Habitos', '/Estadistica']

        # Asignamos el índice basado en la ruta actual
        try:
            self.selected_index = rutas.index(self.page.route)
        except ValueError:
            self.selected_index = 0  # Por si la ruta no coincide

        self.destinations = [
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label='Incio'),
            ft.NavigationBarDestination(icon=ft.Icons.TASK, label='Tareas'),
            ft.NavigationBarDestination(icon=ft.Icons.TRACK_CHANGES, label='Hábitos'),
            ft.NavigationBarDestination(icon=ft.Icons.BAR_CHART, label='Estadística')
        ]
        self.on_change = self.cambiar_ruta

    def cambiar_ruta(self, e):
        opciones = {
            0: '/',
            1: '/Tareas',
            2: '/Habitos',
            3: '/Estadistica'
        }
        self.page.go(opciones[e.control.selected_index])