import flet as ft
from ui.components.button_task import ButtonCrearTarea

class TareasScreen(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.boton_flotante = ft.Column(
            controls=[
                ButtonCrearTarea(page)
            ],
            alignment=ft.MainAxisAlignment.END,
            horizontal_alignment=ft.CrossAxisAlignment.END,
            spacing=10
        )


        self.content = ft.SafeArea(
            content=ft.Stack(
                controls=[
                    ft.Column(
                        scroll=ft.ScrollMode.ADAPTIVE,
                        expand=True,
                        controls=[
                            ft.Text('Texto de prueba de la nueva versión de la página de tareas')
                        ]
                    ),
                    ft.Container(
                        content=self.boton_flotante,
                        bottom=10,
                        right=10
                    )
                ]
            )
        )