import flet as ft

class BarraNavegacionSuperior(ft.AppBar):
    def __init__(self):
        super().__init__()
        
        # 1. Avatar y Texto de bienvenida (lado izquierdo)
        self.leading = ft.Container(
            content=ft.CircleAvatar(
                foreground_image_src='https://raw.githubusercontent.com/SaitoM17/DailyMind/main/src/assets/icons/imagen_perfil_prueba.png',
                content=ft.Text(value='ss'),
                radius=20
            ),
            padding=ft.padding.only(left=10)
        )
        self.leading_width = 50

        self.title = ft.Text(
            value=f'Hola, Said 👋\n¡A darle duro hoy!',
            size=14,
            weight=ft.FontWeight.W_500,
            # line_height=1.2
        )

        # 2. Botón de configuración (lado derecho)
        self.actions = [
            ft.Container(
                content=ft.IconButton(
                    icon=ft.Icons.SETTINGS,
                    icon_color=ft.Colors.BLACK,
                    bgcolor="#ffffff",
                    icon_size=25,
                    on_click=lambda _: print("Configuración clickeada")
                ),
                padding=ft.padding.only(right=10)
            )
        ]
        
        # Configuración visual del AppBar
        self.bgcolor = ft.Colors.TRANSPARENT
        self.center_title = False
        self.toolbar_height = 70 # Un poco más alto para que el texto respire