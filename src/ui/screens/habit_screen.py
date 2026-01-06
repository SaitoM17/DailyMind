import flet as ft

class HabitosScreen(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        texto_prueba = ft.Text('Texto de prueba, pantalla Hábitos')

        self.content = ft.SafeArea(
            content=ft.Stack(
                controls=[
                    ft.Column(
                        scroll=ft.ScrollMode.ADAPTIVE,
                        expand=True,
                        controls=[
                            texto_prueba
                        ]
                    )
                ]
            )
        )