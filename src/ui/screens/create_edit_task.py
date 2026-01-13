import flet as ft
import locale
from datetime import datetime

class CrearEditarEliminarTareaScreen(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = True

        try:
            locale.setlocale(locale.LC_TIME, 'es_ES.utf8') 
        except:
            locale.setlocale(locale.LC_TIME, 'spanish')

        self.estado = {"prioridad": "Media"}

        self.appbar = ft.Row(
            controls=[
                ft.IconButton(
                        icon=ft.Icons.CLEAR,
                        on_click=lambda _: self.page.go('/')
                    ),
                ft.Container(
                    content=ft.Text(
                        'Crear Tarea', 
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

        self.nombre_tarea = ft.Text(value='Nombre de la Tarea')
        self.tarea_input = ft.TextField(label='Ej. Comprar leche', autofocus=True)

        self.descripcion_tarea = ft.Text(value='Descripción')
        self.opcional_descripcion_tarea = ft.Text(value='(Opcional)')
        self.descripcion_input = ft.TextField(label='Añadir detalles...')

        def al_cambiar_fecha(e):
            if self.date_picker.value:
                self.fecha_seleccionada = self.date_picker.value.strftime("%a %d, %b")
                self.texto_fecha.value = self.fecha_seleccionada
                page.update()

        self.date_picker = ft.DatePicker(
            on_change=al_cambiar_fecha,
        )
        page.overlay.append(self.date_picker)

        self.ahora = datetime.now()
        self.ahora_formateado = self.ahora.strftime("%a %d, %b")

        self.texto_fecha = ft.Text(self.ahora_formateado, color=ft.Colors.GREY_700)
        
        self.selector_tarjeta = ft.Container(
            content=ft.ListTile(
                leading=ft.Container(
                    content=ft.Icon(ft.Icons.CALENDAR_MONTH_OUTLINED, color=ft.Colors.BLACK),
                    bgcolor=ft.Colors.YELLOW_100,
                    padding=10,
                    border_radius=25,
                ),
                title=ft.Text("Fecha de vencimiento", weight=ft.FontWeight.BOLD),
                subtitle=self.texto_fecha,
                trailing=ft.Icon(ft.Icons.CHEVRON_RIGHT),
                on_click=lambda _: setattr(self.date_picker, "open", True) or page.update(),
            ),
            border_radius=40,
            padding=ft.padding.symmetric(vertical=5, horizontal=10),
            margin=10,
        )

        # LÓGICA DE PRIORIDAD (DISEÑO SEGMENTADO)
        self.prioridad_container = ft.Container() # Contenedor vacío para refrescar

        def actualizar_prioridad(valor_seleccionado):
            self.estado['prioridad'] = valor_seleccionado
            self.prioridad_container.content = crear_selector_prioridad()
            self.page.update() # Asegúrate de usar self.page

        def crear_selector_prioridad():
            opciones = ['Baja', 'Media', 'Alta']
            botones = []
            
            for opcion in opciones:
                es_sel = opcion == self.estado['prioridad']
                
                botones.append(
                    ft.Container(
                        content=ft.Text(
                            opcion, 
                            color=ft.Colors.BLACK if es_sel else ft.Colors.GREY_700, 
                            weight='bold' if es_sel else 'normal'
                        ),
                        alignment=ft.alignment.center,
                        expand=True,
                        height=40,
                        bgcolor=ft.Colors.WHITE if es_sel else None,
                        border_radius=20,
                        shadow=ft.BoxShadow(blur_radius=4, color=ft.Colors.BLACK12) if es_sel else None,
                        on_click=lambda e, val=opcion: actualizar_prioridad(val)
                    )
                )
                
            return ft.Container(
                content=ft.Row(botones, spacing=0),
                bgcolor='#F2F2E7',
                border_radius=25,
                padding=5,
            )

        self.prioridad_container.content = crear_selector_prioridad()

        # Boton de cancelar tarea
        self.cancelar = ft.ElevatedButton(
            content=ft.Row(
                [
                    ft.Text(value='Cancelar', size=20),
                ],
                tight=True,
                spacing=10
            ),
            expand=1,
            style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=15),
                )
        )

        # Boton de guardar tarea
        self.guardar = ft.ElevatedButton(
            content=ft.Row(
                [
                    ft.Text('Guardar Tarea',size=20),
                ],
                tight=True,
                spacing=10
            ),
            on_click=self.guardar_tarea,
            expand=1,
            style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=15),
                )
        )

        # Contenedor Botones
        self.botones_contenedor = ft.Container(
            ft.Row(
                [
                    self.cancelar,
                    self.guardar
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                alignment=ft.alignment.center,
                adaptive=True
        )

        # Categorias
        self.texto_categorias = ft.Text(value='Categoría')

        self.content = ft.SafeArea(
            content=ft.Stack(
                controls=[
                    ft.Column(
                        scroll=ft.ScrollMode.ADAPTIVE,
                        expand=True,
                        spacing=20,
                        controls=[
                            self.appbar,
                            self.nombre_tarea,
                            self.tarea_input,
                            ft.Row([self.descripcion_tarea, self.opcional_descripcion_tarea]),
                            self.descripcion_input,
                            self.prioridad_container,
                            self.selector_tarjeta,
                            self.texto_categorias,
                            ft.Container(expand=True),
                            self.botones_contenedor
                        ]
                    )
                ]
            )
        )
        
    def guardar_tarea(self, e):
        self.nombre_tarea_input = self.tarea_input.value
        self.descripcion_tarea_input = self.descripcion_input.value
        self.fecha_seleccionada_input = self.texto_fecha.value
        self.priorirdad_tarea_input = self.estado['prioridad']

        print(f'Nombre de tarea: {self.nombre_tarea_input}')
        print(f'Descripción: {self.descripcion_tarea_input}')
        print(f'Fecha de tarea: {self.fecha_seleccionada_input}')
        print(f'Prioridad de tarea: {self.priorirdad_tarea_input}')