import flet as ft


def selecionar_processos(e, elementos):

    elementos.controls.clear()
    elementos.spacing = 30

    if e.control.value == "Calagem":

        if not elementos.controls:
            elementos.controls.append(
                ft.TextField(
                    label="Amostra",
                    hint_text="Ex. Amostra1",
                    border_radius=ft.BorderRadius(10, 10, 10, 10),
                    # 👇 ajustes de cor
                    color="black",  # texto digitado
                    cursor_color="black",  # cursor
                    border_color="black",  # borda normal
                    focused_border_color="black",  # borda quando ativo
                    label_style=ft.TextStyle(color="black"),  # label
                    hint_style=ft.TextStyle(color="gray"),  # placeholder
                    filled=True,
                    fill_color="white",  # fundo branco
                )
            )
            elementos.controls.append(
                ft.TextField(
                    label="Saturação Base",
                    border_radius=ft.BorderRadius(10, 10, 10, 10),
                    hint_text="Ex.%",
                    # 👇 ajustes de cor
                    color="black",  # texto digitado
                    cursor_color="black",  # cursor
                    border_color="black",  # borda normal
                    focused_border_color="black",  # borda quando ativo
                    label_style=ft.TextStyle(color="black"),  # label
                    hint_style=ft.TextStyle(color="gray"),  # placeholder
                    filled=True,
                    fill_color="white",  # fundo branco
                )
            )
            elementos.controls.append(
                ft.TextField(
                    label="CTC pH7",
                    border_radius=ft.BorderRadius(10, 10, 10, 10),
                    hint_text="Ex.cmol/dm³",
                    # 👇 ajustes de cor
                    color="black",  # texto digitado
                    cursor_color="black",  # cursor
                    border_color="black",  # borda normal
                    focused_border_color="black",  # borda quando ativo
                    label_style=ft.TextStyle(color="black"),  # label
                    hint_style=ft.TextStyle(color="gray"),  # placeholder
                    filled=True,
                    fill_color="white",  # fundo branco
                )
            )
            elementos.controls.append(
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="Enviar",
                            expand=True,
                            style=ft.ButtonStyle(
                                bgcolor={
                                    ft.ControlState.DEFAULT: "black",
                                    ft.ControlState.HOVERED: "gray",
                                },
                                color="white",
                                shape=ft.RoundedRectangleBorder(radius=12),
                                elevation={"hovered": 8, "pressed": 2},
                                padding=20,
                            ),
                        )
                    ],
                    expand=True,
                )
            )

    elif e.control.value == "Adubação":

        if not elementos.controls:
            elementos.controls.append(
                ft.TextField(label="Amostra", color=ft.Colors.BLACK)
            ),
            elementos.controls.append(
                ft.TextField(label="Argila", color=ft.Colors.BLACK)
            ),
            elementos.controls.append(
                ft.TextField(label="CTC pH7", color=ft.Colors.BLACK)
            ),
            elementos.controls.append(
                ft.TextField(label="Matéria Orgânica", color=ft.Colors.BLACK)
            ),
            elementos.controls.append(
                ft.TextField(label="Fósforo", color=ft.Colors.BLACK)
            ),
            elementos.controls.append(
                ft.TextField(label="Potássio", color=ft.Colors.BLACK)
            ),
            elementos.controls.append(
                ft.Row(
                    controls=[ft.ElevatedButton(text="Enviar", expand=True)],
                    expand=True,
                )
            )

    elementos.update()
