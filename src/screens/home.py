import flet as ft

def home_page(page: ft.Page):
    
    def go_login(e):
        page.go("/")

    page.clean()

    TopBar= ft.AppBar(
            title=ft.Text("AgroCodeSoil"),bgcolor=ft.Colors.BROWN,
            actions=[
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Sair",on_click=go_login)
                    ]

                )

            ]
                      
        )

    
    Content = ft.Container(






    )
    
    
    DownBar = ft.BottomAppBar(
        
        bgcolor=ft.Colors.BROWN,
        content=ft.ResponsiveRow(

            controls=[

                ft.Row(

                    controls=[

                        ft.Icon(name=ft.Icons.LIST,color=ft.Colors.WHITE,size=30),
                        ft.Icon(name=ft.Icons.HOME,color=ft.Colors.WHITE,size=30),
                        ft.Icon(name=ft.Icons.PICTURE_AS_PDF,color=ft.Colors.WHITE,size=30)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND

                )

            ],
          
        )     
                       
                              
    )


    page.add(
             
        TopBar,
        Content,
        DownBar
   
    )









