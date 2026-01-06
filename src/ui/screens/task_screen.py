import flet as ft
# from ui.components.nav_bar import BarraNavegacion

# class TareasScreen(ft.View):
#     def __init__(self, page: ft.Page):
#         super().__init__(
#             route="/Tareas",
#             navigation_bar=BarraNavegacion(page),
#             padding=20,
#             bgcolor="#F5F5F5",
#             # ¡FALTABA ESTO! Sin controles, la vista es inválida
#             controls=[
#                 ft.AppBar(title=ft.Text("Mis Tareas"), bgcolor=ft.Colors.RED),
#                 ft.Text("Aquí aparecerán tus tareas", size=20)
#             ]
#         )
#         self.page = page

class TareasScreen(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()


        self.content = ft.SafeArea(
            content=ft.Stack(
                controls=[
                    ft.Column(
                        scroll=ft.ScrollMode.ADAPTIVE,
                        expand=True,
                        controls=[
                            ft.Text('Texto de prueba de la nueva versión de la página de tareas')
                        ]
                    )
                ]
            )
        )