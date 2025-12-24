import flet as ft

class DashboarPrincial(ft.Container):
    
    def __init__(self):
        super().__init__()
        
        # self.page.adaptive = True

        #Contenidor 1
        self.texto_bienvenida = ft.Text(value='Hola, Said')
        self.configuracion = ft.Text(value='Icono de configuración')

        # Contenedor 3
        self.dias_racha = ft.Text(value='0')
        self.texto_dias_racha = ft.Text(value='Días Racha')

        # Contenedor 4
        self.fecha_actual = ft.Text(value='\nMié,24 Dic')

        # Contenedor 5 
        self.numero_tareas_pendientes = ft.Text(value='0')
        self.texto_tareas_pendientes = ft.Text(value='Tareas Pendientes')

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
                                ft.Container(self.configuracion)
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
                )
            ])
        )