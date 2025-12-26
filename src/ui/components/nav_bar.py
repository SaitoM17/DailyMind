import flet as ft

class BarraNavegacion(ft.NavigationBar):
    def __init__(self, page: ft.Page):
        super().__init__(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Incio"),
                ft.NavigationBarDestination(icon=ft.Icons.TASK, label="Tareas"),
                ft.NavigationBarDestination(icon=ft.Icons.TRACK_CHANGES,label="Hábitos"),
                ft.NavigationBarDestination(icon=ft.Icons.ANALYTICS, label='Estadística')
            ],
            border=ft.Border(
                top=ft.BorderSide(color=ft.CupertinoColors.SYSTEM_GREY2, width=0)
            )
        )
        
        self.page = page
