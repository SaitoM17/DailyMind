import flet as ft

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
        self.dias_racha = ft.Text(value='0')
        self.texto_dias_racha = ft.Text(value='Días Racha')

        # Contenedor 4
        self.fecha_actual = ft.Text(value='\nMié,24 Dic')

        # Contenedor 5 
        self.numero_tareas_pendientes = ft.Text(value='0')
        self.texto_tareas_pendientes = ft.Text(value='Tareas Pendientes')

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
                                ft.Container(self.dias_racha),
                                ft.Container(self.texto_dias_racha)
                            ]
                        ),
                        ft.Column(
                            spacing=20,
                            controls=[
                                ft.Container(self.fecha_actual)
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
                                ft.Container(self.numero_tareas_pendientes),
                                ft.Container(self.texto_tareas_pendientes)
                            ]
                        )
                    ]
                ),
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