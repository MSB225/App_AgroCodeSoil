import flet as ft

def login_page(page: ft.Page):

    page.bgcolor=ft.Colors.BROWN


    def go_home(e):
        page.go("/home")

    page.clean()

    tela_inicial = ft.Container(
        expand=True,
        content=ft.ResponsiveRow(
           controls=[

                ft.Column(
                    spacing=50,
                    controls=[

                        ft.Text(value="AgroCodeSoil",color=ft.Colors.WHITE,size=50,weight=ft.FontWeight.W_400),
                        ft.Button(text="Entrar",bgcolor=ft.Colors.GREY,color=ft.Colors.BLACK,width=150,on_click=go_home)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER

                )
           ] 

        )

    )

    page.add(tela_inicial) 





