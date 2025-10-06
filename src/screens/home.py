import flet as ft

from components.component_home import criarCampos


def home_page(page: ft.Page):

    def go_login(e):
        page.go("/")

    def nav_changed(e):
        idx = e.control.selected_index
        if idx == 0:
            content.content = home_content
        elif idx == 1:
            content.content = tabela_content
        elif idx == 2:
            content.content = pdf_content
        content.update()  # força a renderização

    page.clean()

    TopBar = ft.AppBar(
        title=ft.Text("AgroCodeSoil"),
        bgcolor=ft.Colors.BROWN,
        actions=[
            ft.PopupMenuButton(items=[ft.PopupMenuItem(text="Sair", on_click=go_login)])
        ],
    )

    elementos = ft.Column()
    conteudo_tabela=ft.Column()

    home_content = ft.Container(
        content=ft.ResponsiveRow(
            controls=[
                ft.Container(
                    padding=20,
                    content=ft.ResponsiveRow(
                        controls=[
                            ft.Text(
                                "Selecione um Processo",
                                color="black",
                                size=12,
                                weight=ft.FontWeight.W_600,
                            ),
                            ft.Dropdown(
                                expand=True,
                                on_change=lambda e: (criarCampos(e,page,elementos,conteudo_tabela)),
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



    tabela_content = ft.Container(
        content=ft.ResponsiveRow(
            controls=[conteudo_tabela]
        )
    )


    pdf_content = ft.Container()

    content = ft.Container(content=home_content)

    pagelet = ft.Pagelet(
        navigation_bar=ft.NavigationBar(
            bgcolor=ft.Colors.BROWN,
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
                ft.NavigationBarDestination(icon=ft.Icons.TABLE_CHART, label="Tabela"),
                ft.NavigationBarDestination(icon=ft.Icons.PICTURE_AS_PDF, label="PDF"),
            ],
            selected_index=0,
            on_change=nav_changed,
        ),
        content=content,
        bgcolor="white",
        expand=True,
    )

    page.add(TopBar, pagelet)
