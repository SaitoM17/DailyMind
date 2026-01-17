import flet as ft

class HabitosScreen(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        texto_prueba = ft.Text('Texto de prueba, pantalla Hábitos')

        # Contenedor 1 Habitos Pendientes
        self.icono_contenedor1 = ft.Icon(name=ft.Icons.VERIFIED, color=ft.Colors.YELLOW, weight=ft.FontWeight.BOLD)
        self.fecha_contenedor1 = ft.Text(value='Hoy', weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
        self.sub_contenedor1 = ft.Row(
            controls=[
                ft.Column(controls=[self.icono_contenedor1], 
                          alignment=ft.MainAxisAlignment.CENTER, 
                          horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                ft.Column(controls=[self.fecha_contenedor1], 
                          alignment=ft.MainAxisAlignment.CENTER, 
                          horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
        self.numerador_habitos = int(1)
        self.denominador_habitos = int(2)
        self.cantidad_habitos = ft.Text(value=f'{self.numerador_habitos}/{self.denominador_habitos}', weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
        self.texto_contenedor1 = ft.Text(value='Hábitos completados', weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)

        self.contenedor_habitos = ft.Container(
            content=ft.Column(
                controls=[
                    self.sub_contenedor1,
                    self.cantidad_habitos,
                    self.texto_contenedor1
                ],
                alignment=ft.alignment.center,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.WHITE,
            border_radius=20
        )

        # Contenedor 2 Racha

        self.icono_contenedor2 = ft.Icon(name=ft.Icons.LOCAL_FIRE_DEPARTMENT, color=ft.Colors.RED, weight=ft.FontWeight.BOLD)
        self.texto_racha = ft.Text(value='RACHA', weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
        self.sub_contenedor2 = ft.Row(
            controls=[
                ft.Column(controls=[self.icono_contenedor2], 
                          alignment=ft.MainAxisAlignment.CENTER, 
                          horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                ft.Column(controls=[self.texto_racha], 
                          alignment=ft.MainAxisAlignment.CENTER, 
                          horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
        self.dias_racha = ft.Text(value='12', weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
        self.texto_contenedor2 = ft.Text(value='Días seguidos', weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)

        self.contenedor_racha = ft.Container(
            content=ft.Column(
                controls=[
                    self.sub_contenedor2,
                    self.dias_racha,
                    self.texto_contenedor2
                ],
                alignment=ft.alignment.center,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.WHITE,
            border_radius=20
        )

        self.content = ft.SafeArea(
            content=ft.Stack(
                controls=[
                    ft.Column(
                        scroll=ft.ScrollMode.ADAPTIVE,
                        expand=True,
                        controls=[
                            texto_prueba,
                            self.contenedor_habitos,
                            self.contenedor_racha
                        ]
                    )
                ]
            )
        )