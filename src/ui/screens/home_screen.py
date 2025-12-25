import flet as ft
import locale
from datetime import datetime

class DashboarPrincial(ft.Container):
    
    def __init__(self):
        super().__init__()
        
        # self.page.adaptive = True

        #Contenidor 1
        self.texto_bienvenida = ft.Text(value='Hola, Said')
        self.boton_configuracion = ft.IconButton(
            icon=ft.Icons.SETTINGS,
            icon_color=ft.Colors.BLACK,
            bgcolor="#ffffff",
            icon_size=30,
        )

        # Contenedor 3
        self.dias_racha = ft.Text(value=f' 🔥  {0} Días Racha ', weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
        self.racha = ft.Container(
            content=self.dias_racha,
            margin=0,
            padding=2,
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.WHITE,
            # width=90,
            height=36,
            border_radius=15,
        )

        # Contenedor 4
        try:
            locale.setlocale(locale.LC_TIME, 'es_ES.utf8') 
        except:
            locale.setlocale(locale.LC_TIME, 'spanish')

        self.ahora = datetime.now()
        self.ahora_formateado = self.ahora.strftime("%a, %d, %b")
        self.fecha_actual = ft.Text(value=f'  📅  {self.ahora_formateado}  ', weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
        self.fecha = ft.Container(
            content=self.fecha_actual,
            margin=0,
            padding=2,
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.WHITE,
            height=36,
            border_radius=15
        )

        # Contenedor 5 
        self.icono_tareas = ft.Text(value='📝', size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
        self.numero_tareas_pendientes = ft.Text('2', size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
        self.texto_tareas_pendientes = ft.Text(value='Tareas Pendientes', weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
        
        self.tareas_pendientes = ft.Container(
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[self.icono_tareas,self.numero_tareas_pendientes]), 
                    self.texto_tareas_pendientes
                    ]
                ),
            margin=0,
            padding=2,
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.WHITE,
            width=140,
            height=90,
            border_radius=15,
            col={"xs": 6, "md": 6, "lg": 4}
        )

        # Contenedor 6 
        self.icono_habitos = ft.Text(value='🔃', size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
        self.numero_habitos_pendientes = ft.Text('4/7', size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
        self.texto_habitos_pendientes = ft.Text(value='Hábitos', weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
        
        self.habitos_pendientes = ft.Container(
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[self.icono_habitos,self.numero_habitos_pendientes]), 
                    self.texto_habitos_pendientes
                    ]
                ),
            margin=0,
            padding=2,
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.WHITE,
            width=140,
            height=90,
            border_radius=15,
            col={"xs": 6, "md": 6, "lg": 4}
        )

        # Contenedor 7
        self.proximas_tareas = ft.Text(value='Próximas Tareas', size=25, weight=ft.FontWeight.BOLD,)

        # Contenedor 8
        self.boton_habitos = ft.ElevatedButton(
            content=ft.Row(
                [
                    ft.Text(value="Hábito", size=16),
                    ft.Icon(name=ft.Icons.SWAP_HORIZ),
                ],
                tight=True,
                spacing=10,
            ),
            style=ft.ButtonStyle(
                color=ft.Colors.BLACK,
                bgcolor="#ffffff",
                shape=ft.RoundedRectangleBorder(radius=15),
            ),
        )
        self.boton_tareas = ft.ElevatedButton(
            content=ft.Row(
                [
                    ft.Text(value='Nueva Tarea', size=18),
                    ft.Icon(name=ft.Icons.ADD)
                ],
                tight=True,
                spacing=10
            ),
            style=ft.ButtonStyle(
                color=ft.Colors.BLACK,
                bgcolor="#ffffff",
                shape=ft.RoundedRectangleBorder(radius=15),
            ),
        )

        # Contenedor 9
        self.navegador_bar = ft.NavigationBar(
            destinations=[
                    ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Incio"),
                    ft.NavigationBarDestination(icon=ft.Icons.TASK, label="Tareas"),
                    ft.NavigationBarDestination(icon=ft.Icons.TRACK_CHANGES,label="Hábitos"),
                    ft.NavigationBarDestination(icon=ft.Icons.ANALYTICS, label='Estadística')
                ],
            border=ft.Border(
                top=ft.BorderSide(color=ft.CupertinoColors.SYSTEM_GREY2, width=0)
            ),
        )


        self.content = ft.SafeArea(
            ft.Column([
                ft.Row(
                    spacing=20,
                    controls=[
                        ft.Column(
                            spacing=20,
                            controls=[
                                ft.Container(self.texto_bienvenida)
                            ]
                        ),
                        ft.Column(
                            spacing=20,
                            controls=[
                                ft.Container(self.boton_configuracion, padding=0)
                            ]
                        )
                    ]
                ),
                ft.Row(
                    spacing=20,
                    controls=[
                        ft.Column(
                            spacing=0,
                            controls=[
                                ft.Container(self.racha)
                            ]
                        ),
                        ft.Column(
                            spacing=20,
                            controls=[
                                ft.Container(self.fecha)
                            ]
                        )
                    ]
                ),
                ft.ResponsiveRow(
                    controls=[
                        self.tareas_pendientes,
                        self.habitos_pendientes
                    ],
                    spacing=20,
                    run_spacing=20
                ),
                self.proximas_tareas,
                ft.Row(
                    spacing=20,
                    controls=[
                        ft.Column(
                            spacing=20,
                            controls=[
                                ft.Container(self.boton_habitos),
                                ft.Container(self.boton_tareas)
                            ]
                        )
                    ]
                ),
                self.navegador_bar
            ])
        )                        