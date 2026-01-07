import flet as ft
import locale
from datetime import datetime

def CrearEditarEliminarTareaScreen(page: ft.Page):

    try:
        locale.setlocale(locale.LC_TIME, 'es_ES.utf8') 
    except:
        locale.setlocale(locale.LC_TIME, 'spanish')

    estado = {"prioridad": "Media"}
    
    appbar = ft.AppBar(
        leading=ft.IconButton(
            ft.Icons.CLEAR,
            icon_size=25, 
            on_click=lambda _:page.go('/')
            ),
            title=ft.Text('Crear Tarea'),
            center_title=True,
            bgcolor=ft.Colors.with_opacity(0.04, ft.CupertinoColors.SYSTEM_BACKGROUND),
    )

    nombre_tarea = ft.Text(value='Nombre de la Tarea')
    tarea_input = ft.TextField(label='Ej. Comprar leche', autofocus=True)

    descripcion_tarea = ft.Text(value='Descripción')
    opcional_descripcion_tarea = ft.Text(value='(Opcional)')
    descripcion_input = ft.TextField(label='Añadir detalles...')

    def al_cambiar_fecha(e):
        if date_picker.value:
            fecha_seleccionada = date_picker.value.strftime("%a %d, %b")
            texto_fecha.value = fecha_seleccionada
            page.update()

    date_picker = ft.DatePicker(
        on_change=al_cambiar_fecha,
    )
    page.overlay.append(date_picker)

    ahora = datetime.now()
    ahora_formateado = ahora.strftime("%a %d, %b")

    texto_fecha = ft.Text(ahora_formateado, color=ft.Colors.GREY_700)
    
    selector_tarjeta = ft.Container(
        content=ft.ListTile(
            leading=ft.Container(
                content=ft.Icon(ft.Icons.CALENDAR_MONTH_OUTLINED, color=ft.Colors.BLACK),
                bgcolor=ft.Colors.YELLOW_100,
                padding=10,
                border_radius=25,
            ),
            title=ft.Text("Fecha de vencimiento", weight=ft.FontWeight.BOLD),
            subtitle=texto_fecha,
            trailing=ft.Icon(ft.Icons.CHEVRON_RIGHT),
            on_click=lambda _: setattr(date_picker, "open", True) or page.update(),
        ),
        border_radius=40,
        padding=ft.padding.symmetric(vertical=5, horizontal=10),
        margin=10,
    )

    # LÓGICA DE PRIORIDAD (DISEÑO SEGMENTADO)
    prioridad_container = ft.Container() # Contenedor vacío para refrescar

    def actualizar_prioridad(valor):
        estado["prioridad"] = valor
        prioridad_container.content = crear_selector_prioridad()
        page.update()

    def crear_selector_prioridad():
        opciones = ["Baja", "Media", "Alta"]
        botones = []
        for op in opciones:
            es_sel = op == estado["prioridad"]
            botones.append(
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
            content=ft.Row(botones, spacing=0),
            bgcolor="#F2F2E7",
            border_radius=25,
            padding=5,
        )

    prioridad_container.content = crear_selector_prioridad()
    
    def guardar_tarea(e):
        print(f"Tarea guardada: {tarea_input.value}")
        page.go("/") # Regresa al inicio tras guardar

    return ft.View(
        "/create",
        controls=[
            appbar,
            ft.SafeArea(
                content=ft.Column([                    
                    nombre_tarea,
                    tarea_input,
                    ft.Row([
                        descripcion_tarea,
                        opcional_descripcion_tarea,
                    ]),
                    descripcion_input,
                    prioridad_container,
                    selector_tarjeta,
                    ft.ElevatedButton("Guardar Tarea", on_click=guardar_tarea)
                ], spacing=20)
            )
        ]
    )