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

        self.estado = {'prioridad': 'Todas'}

        self.prioridad_container = ft.Container() # Contenedor vacío para refrescar

        def actualizar_prioridad(valor):
            self.estado['prioridad'] = valor
            self.prioridad_container.content = crear_selector_prioridad()
            page.update()

        def crear_selector_prioridad():
            self.opciones = ['Todas', 'Pendientes', 'Completadas']
            self.botones = []
            for op in self.opciones:
                es_sel = op == self.estado['prioridad']
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

        self.selector_fecha = ft.Dropdown(
            label='Fecha',
            options=[
                ft.Text('08, jue, ene')
            ]
        )

        self.prioridad = ['Baja', 'Mediana', 'Alta']

        def get_options():
            self.opciones = []
            for self.op in self.prioridad:
                self.opciones.append(
                    ft.DropdownOption(self.op)
                )

        self.selector_prioridad = ft.Dropdown(
            label='Priodad',
            options=[
                ft.DropdownOption('Baja'),
                ft.DropdownOption('Media'),
                ft.DropdownOption('Alta')
            ]
        )

        self.selector_categoria = ft.Dropdown(
            label='Categoría',
            options=[
                ft.DropdownOption('Trabajo'),
                ft.DropdownOption('Escuela'),
                ft.DropdownOption('Hogar')
            ]
        )
        # self.racha = ft.Container(
        #     content=self.dias_racha,
        #     margin=0,
        #     padding=2,
        #     # alignment=ft.alignment.center,
        #     # bgcolor=ft.Colors.WHITE,
        #     # width=90,
        #     height=36,
        #     border_radius=15,
        # )



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
                            self.prioridad_container,
                            self.selector_fecha,
                            self.selector_prioridad,
                            self.selector_categoria
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