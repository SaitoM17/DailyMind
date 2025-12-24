import flet as ft

class DashboarPrincial(ft.Container):
    
    def __init__(self):
        super().__init__()
        
        #Contenidor 1
        self.texto_bienvenida = ft.Text(value='Hola, Said')
        self.configuracion = ft.Text(value='Icono de configuración')

        self.content = ft.Row(
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
            )]
        )