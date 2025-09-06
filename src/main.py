import flet as ft
from screens.login import login_page
from screens.home import home_page


def main(page: ft.Page):

    page.padding = 0

    def route_change(route):

        if page.route == "/":
            login_page(page)

        elif page.route == "/home":
            home_page(page)

        page.update()

    page.on_route_change = route_change
    page.go("/")  # inicia sempre na rota inicial


ft.app(target=main)
