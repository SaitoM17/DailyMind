import flet as ft
from ui.screens.home_screen import DashboarPrincial
from ui.components.nav_bar import BarraNavegacion

def main(page: ft.Page):
    # page.scroll = True

    nav = BarraNavegacion(page)
    app = DashboarPrincial()

    page.navigation_bar = nav
    page.add(app)


ft.app(target=main)
