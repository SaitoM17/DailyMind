import flet as ft

class ButtonCrearHabito(ft.ElevatedButton):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        self.content=ft.Row(
            [
                ft.Text(value='Hábito', size=18),
                ft.Icon(name=ft.Icons.SWAP_HORIZ)
            ],
            tight=True,
            spacing=10
        )
        self.on_click = self.nuevo_habito
        self.style=ft.ButtonStyle(
                color=ft.Colors.BLACK,
                bgcolor="#ffffff",
                shape=ft.RoundedRectangleBorder(radius=15),
            )

    def nuevo_habito(self, e):
        self.page.client_storage.set('return_route', self.page.route)
        self.page.go("/CreateHabito")