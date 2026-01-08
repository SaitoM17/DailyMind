import flet as ft

class CrearEditarEliminarHabitoScreen(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.expand = True # Para que ocupe todo el espacio en el View

        # Componentes de la interfaz
        self.task_input = ft.TextField(
            label='¿Qué hay que hacer?', 
            autofocus=True,
            border_color='blue'
        )

        self.appbar = ft.Row(
            controls=[
                ft.IconButton(
                        icon=ft.Icons.CLEAR,
                        on_click=lambda _: self.page.go('/')
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
                            # Cuerpo del formulario
                            ft.Text('Detalles del Hábito', size=18),
                            self.task_input,
                            ft.ElevatedButton(
                                text='Guardar Hábito',
                                on_click=self.guardar_habito
                            )
                        ]
                    )
                ]
            )
        )

    def guardar_habito(self, e):
        print(f'Hábito guardado: {self.task_input.value}')
        self.page.go('/')