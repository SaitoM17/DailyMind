import sys
import flet as ft
from ui.screens.home_screen import DashboardPrincial
from ui.components.nav_bar import BarraNavegacion
from ui.screens.task_screen import TareasScreen
from ui.components.app_bar import BarraNavegacionSuperior
from ui.screens.habit_screen import HabitosScreen
from ui.screens.progress_statistics_screen import EstadisticasProgresoScreen
from ui.screens.create_edit_task import CrearEditarEliminarTareaScreen
from ui.screens.create_edit_habit import CrearEditarEliminarHabitoScreen

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def main(page: ft.Page):
    page.title = "Mi App Estructurada"

    # FUNCIÓN CLAVE: Aquí se decide qué vistas (capas) mostrar
    def route_change(route):
        page.views.clear() # Limpiamos la pila
        
        # 1. Siempre ponemos el Inicio como base de la pila
        page.views.append(
            ft.View(
                route="/",
                controls=[
                    BarraNavegacionSuperior(),
                    DashboardPrincial(page),                    
                    ],
                    navigation_bar=BarraNavegacion(page),         
            )
        )
        
        # Vista de Tareas
        if page.route == "/Tareas":
            page.views.append(
                ft.View(
                    "/Tareas",
                    [
                        BarraNavegacionSuperior(),
                        TareasScreen(page),
                    ],
                    BarraNavegacion(page)
                )
            )
        
        # Vista de Hábitos
        elif page.route == '/Habitos':
            page.views.append(
                ft.View(
                    '/Habitos',
                    [
                        BarraNavegacionSuperior(),
                        HabitosScreen(page),
                    ],
                    BarraNavegacion(page)
                )
            )
        
        # Vista de Estadistica y progreso
        elif page.route == '/Estadistica':
            page.views.append(
                ft.View(
                    '/Estadistica',
                    [
                        BarraNavegacionSuperior(),
                        EstadisticasProgresoScreen(page),
                    ],
                    BarraNavegacion(page)
                )
            )
        
        elif page.route == "/create":
            page.views.append(CrearEditarEliminarTareaScreen(page))

        elif page.route == "/CreateHabito":
            page.views.append(CrearEditarEliminarHabitoScreen(page))
            
        page.update()

    # Maneja el botón "Atrás" del sistema (Android o Navegador)
    def view_pop(e): # Flet pasa un evento aquí
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)
        else:
            # Si no hay más vistas, regresa al inicio por defecto
            page.go("/")

    # Registramos los eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    # Lanzamos la app
    page.go(page.route)

ft.app(target=main)
