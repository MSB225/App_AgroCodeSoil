import flet as ft

from components.component_home import selecionar_processos


def home_page(page: ft.Page):



    def go_login(e):
        page.go("/")

    page.clean()

    TopBar = ft.AppBar(
        title=ft.Text("AgroCodeSoil"),
        bgcolor=ft.Colors.BROWN,
        actions=[
            ft.PopupMenuButton(items=[ft.PopupMenuItem(text="Sair", on_click=go_login)])
        ],
    )

    elementos = ft.Column()

    Content = ft.Container(
        expand=True,
        bgcolor=ft.Colors.WHITE,
        content=ft.ResponsiveRow(
            controls=[
                ft.Container(
                    padding=20,
                    content=ft.ResponsiveRow(
                        controls=[
                            ft.Text("Selecione um Processo",color="black",size=12,weight=ft.FontWeight.W_600),
                            ft.Dropdown(
                                expand=True,
                                on_change=lambda e: selecionar_processos(e, elementos),
                                label_content="Defina o Processo",
                                color="black",
                                options=[
                                    ft.dropdown.Option(key="Calagem"),
                                    ft.dropdown.Option(key="Adubação"),
                                ],
                            ),
                        ]
                    ),
                ),
                ft.Container(
                    padding=20, content=ft.ResponsiveRow(controls=[elementos])
                ),
            ]
        ),
    )

    DownBar = ft.BottomAppBar(
        bgcolor=ft.Colors.BROWN,
        content=ft.ResponsiveRow(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(name=ft.Icons.LIST, color=ft.Colors.WHITE, size=30),
                        ft.Icon(name=ft.Icons.HOME, color=ft.Colors.WHITE, size=30),
                        ft.Icon(
                            name=ft.Icons.PICTURE_AS_PDF, color=ft.Colors.WHITE, size=30
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
            ],
        ),
    )

    page.add(TopBar, Content, DownBar)
