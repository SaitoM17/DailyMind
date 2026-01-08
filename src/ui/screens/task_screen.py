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

        self.estado = {"prioridad": "Todas"}

        self.prioridad_container = ft.Container() # Contenedor vacío para refrescar

        def actualizar_prioridad(valor):
            self.estado["prioridad"] = valor
            self.prioridad_container.content = crear_selector_prioridad()
            page.update()

        def crear_selector_prioridad():
            self.opciones = ["Baja", "Media", "Alta"]
            self.botones = []
            for op in self.opciones:
                es_sel = op == self.estado["prioridad"]
                self.botones.append(
                    ft.Container(
                        content=ft.Text(op, color=ft.Colors.BLACK if es_sel else ft.Colors.GREY_700, weight="bold" if es_sel else "normal"),
                        alignment=ft.alignment.center,
                        expand=True,
                        height=40,
                        bgcolor=ft.Colors.WHITE if es_sel else None,
                        border_radius=20,
                        shadow=ft.BoxShadow(blur_radius=4, color=ft.Colors.BLACK12) if es_sel else None,
                        on_click=lambda e, val=op: actualizar_prioridad(val)
                    )
                )
            return ft.Container(
                content=ft.Row(self.botones, spacing=0),
                bgcolor="#F2F2E7",
                border_radius=25,
                padding=5,
            )
        
        self.prioridad_container.content = crear_selector_prioridad()


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
                            ),
                            self.prioridad_container
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