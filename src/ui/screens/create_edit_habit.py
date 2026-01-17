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

        # Medición
        self.texto_medicion = ft.Text(value='¿Cómo quieres medirlo?')        
        self.contenedor_medicion = ft.RadioGroup(
            content=ft.Row(
                [
                    ft.Radio(
                        value="1",
                        label="Completar (sí/no)",
                        adaptive= True,
                        active_color=ft.Colors.GREEN,
                    ),
                    ft.Radio(
                        value="2",
                        label="Medible",
                        adaptive=True,
                        active_color=ft.Colors.BLUE,
                    ),
                ]
            )
        )

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
                            self.habito_input,
                            self.texto_medicion,
                            self.contenedor_medicion
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