import flet as ft

class CrearEditarEliminarHabitoScreen(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.expand = True 

        self.appbar = ft.Row(
            controls=[
                ft.IconButton(
                        icon=ft.Icons.CLEAR,
                        on_click=lambda _: self.volver()
                    ),
                ft.Container(
                    content=ft.Text(
                        'Crear Hábito', 
                        size=20, 
                        weight='bold',
                        text_align=ft.TextAlign.CENTER # Centra el texto dentro del container
                    ),
                    expand=True, # Ocupa todo el espacio sobrante
                    margin=ft.margin.only(right=40) # Compensa el ancho del icono izquierdo para un centrado perfecto
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )

        # Nombre del hábito
        self.nombre_habito = ft.Text(value='Nombre del Hábito')
        self.habito_input = ft.TextField(label='Ej. Leer 10 páginas', autofocus=True)

        # Definimos el contenido siguiendo tu estructura
        self.content = ft.SafeArea(
            content=ft.Stack(
                controls=[
                    ft.Column(
                        scroll=ft.ScrollMode.ADAPTIVE,
                        expand=True,
                        spacing=20,
                        controls=[
                            self.appbar,                            
                            self.nombre_habito,
                            self.habito_input
                        ]
                    )
                ]
            )
        )

    def guardar_habito(self, e):
        print(f'Hábito guardado: {self.task_input.value}')
        self.page.go('/')

    def cancelar_tarea(self, e):
        self.volver()
    
    def volver(self):
        return_route = self.page.client_storage.get('return_route') or '/'
        self.page.go(return_route)