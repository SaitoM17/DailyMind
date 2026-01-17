import flet as ft
from ui.components.button_task import ButtonCrearTarea
import database

class TareasScreen(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.expand = True

        self.cantidad_tareas_pendinetes = '4'
        self.tareas_pendientes = ft.Text(value=f'Tienes {self.cantidad_tareas_pendinetes} tareas pendientes')

        self.boton_flotante = ft.Column(
            controls=[
                ButtonCrearTarea(page)
            ],
            alignment=ft.MainAxisAlignment.END,
            horizontal_alignment=ft.CrossAxisAlignment.END,
            spacing=10
        )

        self.estado = {'prioridad': 'Todas'}

        self.prioridad_container = ft.Container() # Contenedor vacío para refrescar

        def actualizar_prioridad(valor):
            self.estado['prioridad'] = valor
            self.prioridad_container.content = crear_selector_prioridad()
            page.update()

        def crear_selector_prioridad():
            self.opciones = ['Todas', 'Pendientes', 'Completadas']
            self.botones = []
            for op in self.opciones:
                es_sel = op == self.estado['prioridad']
                self.botones.append(
                    ft.Container(
                        content=ft.Text(op, color=ft.Colors.BLACK if es_sel else ft.Colors.GREY_700, weight="bold" if es_sel else "normal"),
                        alignment=ft.alignment.center,
                        expand=True,
                        height=40,
                        bgcolor=ft.Colors.WHITE if es_sel else None,
                        border_radius=20,
                        shadow=ft.BoxShadow(blur_radius=4, color=ft.Colors.BLACK12) if es_sel else None,
                        on_click=lambda e, val=op: actualizar_prioridad(val)
                    )
                )
            return ft.Container(
                content=ft.Row(self.botones, spacing=0),
                bgcolor="#F2F2E7",
                border_radius=25,
                padding=5,
            )
        
        self.prioridad_container.content = crear_selector_prioridad()

        self.selector_fecha = ft.Dropdown(
            label=ft.Text('Fecha', size=10),
            border_width=0,
            border_radius=15,
            options=[
                ft.DropdownOption('08, jue, ene')
            ]
        )

        self.prioridad = ['Baja', 'Mediana', 'Alta']

        def get_options():
            self.opciones = []
            for self.op in self.prioridad:
                self.opciones.append(
                    ft.DropdownOption(self.op)
                )

        self.selector_prioridad = ft.Dropdown(
            label=ft.Text('Priodad', size=10),
            border_width=0,
            border_radius=15,
            options=[
                ft.DropdownOption('Baja'),
                ft.DropdownOption('Media'),
                ft.DropdownOption('Alta')
            ]
        )

        self.selector_categoria = ft.Dropdown(
            label=ft.Text('Categoría', size=10),
            border_width=0,
            border_radius=15,
            options=[
                ft.DropdownOption('Trabajo'),
                ft.DropdownOption('Escuela'),
                ft.DropdownOption('Hogar')
            ]
        )
        
        self.contenedor_fecha = ft.Container(
            content=self.selector_fecha,
            col=4,
            alignment=ft.alignment.center
        )

        self.contenedor_prioridad = ft.Container(
            content=self.selector_prioridad,
            col=4,
            alignment=ft.alignment.center
        )

        self.contenedor_categoria = ft.Container(
            content=self.selector_categoria,
            col=4,
            alignment=ft.alignment.center
        )

        self.fila_desplegables = ft.ResponsiveRow(
            controls=[
                self.contenedor_fecha,
                self.contenedor_prioridad,
                self.contenedor_categoria
            ],
            spacing=2,       # Espacio pequeño entre botones para que no se amontonen
            run_spacing=0,   # Evitamos que salten de línea
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        self.tareas_container = ft.Container()
        self.tarea_seleccionada = None

        self.tareas_container.content = self.crear_lista_tareas()
    
        self.content = ft.SafeArea(
            content=ft.Stack(
                controls=[
                    ft.Column(
                        scroll=ft.ScrollMode.ADAPTIVE,
                        expand=True,
                        controls=[
                            ft.Row(
                                spacing=20,
                                controls=[ft.Container(self.tareas_pendientes)]
                            ),
                            self.prioridad_container,
                            ft.Container(
                                padding=ft.padding.symmetric(horizontal=5),
                                content=self.fila_desplegables
                            ),
                            self.tareas_container                            
                        ]
                    ),
                    ft.Container(
                        content=self.boton_flotante,
                        bottom=10,
                        right=10
                    )
                ],
                expand=True
            )
        )

    def seleccionar_tarea(self, tarea):
        self.tarea_seleccionada = tarea
        self.tareas_container.content = self.crear_lista_tareas()
        self.page.update()
        self.abrir_detalles(tarea)

    def abrir_detalles(self, tarea):
        def cerrar(e):
            dialogo.open = False
            self.page.update()

        def editar(e):
            cerrar(e)
            self.page.go(f'/edit?nombre={tarea["nombre"]}')

        def eliminar(e):
            tareas = database.get('mis_tareas') or []
            tareas = [t for t in tareas if t != tarea]
            database.set('mis_tareas', tareas)

            self.tarea_seleccionada = None
            self.refrescar_lista()
            cerrar(e)

        dialogo = ft.AlertDialog(
            modal=True,
            title=ft.Text(tarea['nombre']),
            content=ft.Column(
                [
                    ft.Text(f'📅 Fecha: {tarea['fecha']}'),
                    ft.Text(f'🔥 Prioridad: {tarea['prioridad']}'),
                    ft.Text(f'📝 Descripción: {tarea.get('descripcion', 'Sin descripción')}'),
                ],
                tight=True,
            ),
            actions=[
                ft.TextButton('Cerrar', on_click=cerrar),
                ft.OutlinedButton('Eliminar', icon=ft.Icons.DELETE, on_click=eliminar),
                ft.ElevatedButton('Editar', icon=ft.Icons.EDIT, on_click=editar),
            ],
        )

        self.page.overlay.clear()
        self.page.overlay.append(dialogo)
        dialogo.open = True
        self.page.update()


    def refrescar_lista(self):
        self.tareas_container.content = self.crear_lista_tareas()
        self.page.update()

    def crear_lista_tareas(self):
        tareas = database.get('mis_tareas') or []

        lista = ft.Column(spacing=10)

        for t in tareas:
            seleccionada = self.tarea_seleccionada == t

            lista.controls.append(
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Checkbox(value=t['completada']),
                            ft.Column(
                                [
                                    ft.Text(t['nombre'], weight='bold'),
                                    ft.Text(
                                        f"{t['categoria']} | {t['fecha']} | {t['prioridad']}",
                                        size=12,
                                        color=ft.Colors.GREY_700
                                    )
                                ],
                                spacing=2
                            )
                        ],
                        spacing=10
                    ),
                    padding=10,
                    bgcolor=ft.Colors.BLUE_50 if seleccionada else ft.Colors.WHITE,
                    border_radius=12,
                    border=ft.border.all(
                        2 if seleccionada else 1,
                        ft.Colors.BLUE if seleccionada else ft.Colors.BLACK12
                    ),
                    on_click=lambda e, t=t: self.seleccionar_tarea(t)
                )
            )

                
        lista.controls.append(ft.Container(height=50))

        return lista