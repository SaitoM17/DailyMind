import flet as ft
from ui.components.button_task import ButtonCrearTarea

class TareasScreen(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.cantidad_tareas_pendinetes = '4'
        self.tareas_pendientes = ft.Text(value=f'Tienes {self.cantidad_tareas_pendinetes} tareas pendientes')

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
                            ft.Row(
                                spacing=20,
                                controls=[ft.Container(self.tareas_pendientes)]
                            )
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