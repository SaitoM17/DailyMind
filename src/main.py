import flet as ft
from ui.screens.home_screen import DashboarPrincial

def main(page: ft.Page):
    page.adaptive = True
    app = DashboarPrincial()

    page.add(app)


ft.app(target=main)
