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

        # Frecuencia
        self.frecuencia_contenedor = ft.Container()
        self.estado_frecuencia = {'frecuencia': 'Diaria'}
        self.frecuencia_contenedor.content = self.crear_selector_frecuencia(self.estado_frecuencia)

        # Calendario - semana
        self.semana_contenedor = ft.Container()
        self.estado_semana = {'semana': 'Lunes'}
        self.semana_contenedor.content = self.crear_selector_semana(self.estado_semana)

        # Medición - Medible
        self.titulo_medible = ft.Text(value='Meta')
        self.input_medibles = ft.TextField(
            border_radius=10
        )
        
        self.lista_medibles = ft.Dropdown(
            border_radius=10,
            options=[
                ft.DropdownOption(key='Páginas'),
                ft.DropdownOption(key='Veces'),
                ft.DropdownOption(key='Minutos')
            ]
        )

        self.sub_contenedor_input_medible = ft.Container(
            content=self.input_medibles,
            col=4,
            alignment=ft.alignment.center
        )

        self.sub_contenedor_lista_medible = ft.Container(
            content=self.lista_medibles,
            col=4,
            alignment=ft.alignment.center
        )

        self.contenedor_medible = ft.ResponsiveRow(
            controls=[
                self.titulo_medible,
                self.sub_contenedor_input_medible,
                self.sub_contenedor_lista_medible,
            ],
            spacing=10,
            run_spacing=0,
            alignment=ft.MainAxisAlignment.START
        )

        # Recordatorio
        self.titulo_recordatorio = ft.Text(value='Recodatorio')
        self.texto_recordatorio = ft.Text(value='Activar recordatorio', color=ft.Colors.BLACK)
        self.texto_reci_notific = ft.Text(value='Recibe notificación', color=ft.Colors.BLACK)
        self.swicht_on_off = ft.Switch()

        self.icono_hora = ft.Icon(name=ft.Icons.ACCESS_TIME_FILLED, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD)
        self.texto_hora = ft.Text(value='Hora', color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD)

        self.hora = ft.Text(value='09 : 00 AM', color=ft.Colors.GREY_500)
        self.contenedor_hora = ft.Container(
            content=self.hora,
            bgcolor="#F5F5F5",  
            padding=ft.padding.symmetric(horizontal=35, vertical=10),            
            border_radius=30,    
            alignment=ft.alignment.center,
            on_click=self.abrir_reloj
        )
        self.reloj_input = ft.TimePicker(
            confirm_text="Confirmar",
            error_invalid_text="Time out of range",
            help_text="Seleccionar hora",
            on_change=self.cambiar_hora,
            time_picker_entry_mode=ft.TimePickerEntryMode.INPUT_ONLY
        )

        self.page.overlay.append(self.reloj_input)


        self.contenedor_recordatorio = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Column(
                                controls=[self.texto_recordatorio, self.texto_reci_notific],
                                expand=True,
                                spacing=0,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            ft.Column(
                                controls=[self.swicht_on_off],
                                expand=True,
                                alignment=ft.alignment.center,
                                horizontal_alignment=ft.CrossAxisAlignment.END                        
                            )
                        ],
                        expand=True                        
                    ),
                    ft.Divider(height=1, thickness=1, color="grey"),
                    ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            self.icono_hora,
                                            self.texto_hora
                                        ]
                                    )
                                ]
                            ),
                            ft.Column(
                                controls=[self.reloj_input, self.contenedor_hora]
                            )
                        ]
                    )                    
                ],
                # expand=True
            ),
            padding=10,
            # margin=10,
            bgcolor=ft.Colors.WHITE,
            border_radius=10
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
                            self.contenedor_medicion,
                            self.frecuencia_contenedor,
                            self.semana_contenedor,                            
                            ft.Container(
                                padding=ft.padding.symmetric(horizontal=5),
                                content=self.contenedor_medible
                            ),
                            self.contenedor_recordatorio,
                            ft.ElevatedButton(
                                text='Guardar',
                                on_click=self.guardar_habito
                            )
                        ]
                    )
                ]
            )
        )

    def guardar_habito(self, e):
        print(f'Hábito guardado: {self.habito_input.value}')

        if self.contenedor_medicion.value == '1':
            print(f'Medición: Completar (sí/no)')
        else:
            print(f'Medición: Medible')
        
        self.volver()

    def cancelar_tarea(self, e):
        self.volver()
    
    def volver(self):
        return_route = self.page.client_storage.get('return_route') or '/'
        self.page.go(return_route)
    
    def actualizar_frecuencia(self, valor_seleccionado):
        self.estado_frecuencia['frecuencia'] = valor_seleccionado
        self.frecuencia_contenedor.content = self.crear_selector_frecuencia(estado_frecuencia=self.estado_frecuencia)
        self.page.update() 

    def crear_selector_frecuencia(self, estado_frecuencia):
        opciones = ['Diaria', 'Semanal']
        botones = []
            
        for opcion in opciones:
            es_sel = opcion == self.estado_frecuencia['frecuencia']
                
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
                    on_click=lambda e, val=opcion: self.actualizar_frecuencia(val)
                )
            )
                
        return ft.Container(
            content=ft.Row(botones, spacing=0),
            bgcolor='#F2F2E7',
            border_radius=25,
            padding=5,
        )
    
    def actualizar_semana(self, valor_seleccionado):
        self.estado_semana['semana'] = valor_seleccionado
        self.semana_contenedor.content = self.crear_selector_semana(estado_semana=self.estado_semana)
        self.page.update() 

    def crear_selector_semana(self, estado_semana):
        opciones = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        botones = []
            
        for opcion in opciones:
            es_sel = opcion == estado_semana['semana']
                
            botones.append(
                ft.Container(
                    content=ft.Text(
                        opcion, 
                        color=ft.Colors.BLACK if es_sel else ft.Colors.GREY_700, 
                        weight='bold' if es_sel else 'normal',
                        size=10
                    ),
                    alignment=ft.alignment.center,
                    expand=True,
                    height=40,
                    bgcolor=ft.Colors.WHITE if es_sel else None,
                    border_radius=20,
                    shadow=ft.BoxShadow(blur_radius=4, color=ft.Colors.BLACK12) if es_sel else None,
                    on_click=lambda e, val=opcion: self.actualizar_semana(val)
                )
            )
                
        return ft.Container(
            content=ft.Row(botones, spacing=0),
            bgcolor='#F2F2E7',
            border_radius=25,
            padding=5,
        )

    def abrir_reloj(self, _):
        self.reloj_input.open = True
        self.page.update()

    def cambiar_hora(self, e):
        if self.reloj_input.value:
            t = self.reloj_input.value
                        
            hora_12 = t.hour if 0 < t.hour <= 12 else (t.hour - 12 if t.hour > 12 else 12)
            periodo = "AM" if t.hour < 12 else "PM"
                        
            self.hora_seleccionada = f"{hora_12:02d} : {t.minute:02d} {periodo}"
            
            self.hora.value = self.hora_seleccionada
            self.page.update()