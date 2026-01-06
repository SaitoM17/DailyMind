import sys
import flet as ft
from ui.screens.home_screen import DashboardPrincial
from ui.components.nav_bar import BarraNavegacion
from ui.screens.task_screen import TareasScreen
from ui.components.app_bar import BarraNavegacionSuperior

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def main(page: ft.Page):
    page.title = "Mi App Estructurada"

    # FUNCIÓN CLAVE: Aquí se decide qué vistas (capas) mostrar
    def route_change(route):
        page.views.clear() # Limpiamos la pila
        
        # 1. Siempre ponemos el Inicio como base de la pila
        if page.route == "/":
            page.views.append(
                ft.View(
                    route="/",
                    controls=[
                        BarraNavegacionSuperior(),
                        DashboardPrincial(page)
                        ],                    
                    navigation_bar=BarraNavegacion(page)
                )
            )
        
        # Vista de Tareas
        elif page.route == "/Tareas":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        BarraNavegacionSuperior(),
                        TareasScreen(page),
                    ],
                    BarraNavegacion(page)
                )
            )
        # page.update()
            
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
