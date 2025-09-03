import flet as ft

elementos = ft.Column()


def selecionar_processos(e):

    elementos.controls.clear()
    elementos.spacing = 30

    if e.control.value == "Calagem":

        if not elementos.controls:
            elementos.controls.append(ft.TextField(label="Amostra"))
            elementos.controls.append(ft.TextField(label="Saturação Base"))
            elementos.controls.append(ft.TextField(label="CTC pH7"))
            elementos.controls.append(ft.ElevatedButton(text="Enviar"))

    elif e.control.value == "Adubação":

        if not elementos.controls:
            elementos.controls.append(ft.TextField(label="Amostra")),
            elementos.controls.append(ft.ElevatedButton(text="Enviar"))

    elementos.update()
