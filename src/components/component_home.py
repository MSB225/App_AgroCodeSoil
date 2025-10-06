import flet as ft
import json

from logics.interpretation import interpretar_saturação_por_bases , interpretar_ctc_ph7

array_dados=[]

def criarCampos(e,page,elementos,conteudo_tabela):

    elementos.controls.clear()
    elementos.spacing = 30

    amostra = ft.TextField(
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

    saturacao_base = ft.TextField(
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
    ctc_ph7 = ft.TextField(
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

    botao = ft.Row(
        controls=[
            ft.ElevatedButton(
                text="Enviar",
                on_click=lambda e: guardarValores(e,page,amostra,saturacao_base,ctc_ph7,conteudo_tabela),
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

    if e.control.value == "Calagem":

        if not elementos.controls:
            elementos.controls.append(amostra)
            elementos.controls.append(saturacao_base)
            elementos.controls.append(ctc_ph7)
            elementos.controls.append(botao)

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

 
def guardarValores(e,page,amostra,saturacao_base,ctc_ph7,conteudo_tabela):

    json_string_salva = page.client_storage.get("dados_calagem")

    # Converte para a lista Python (array) ou inicializa como lista vazia
    if json_string_salva:
        lista_registros = json.loads(json_string_salva)
    else:
        # Se for a primeira vez, cria a lista vazia
        lista_registros = []

    amostraCalagem = amostra.value
    saturacaoBase = saturacao_base.value
    ctcpH7 = ctc_ph7.value

    dados = {
        "amostra": amostraCalagem,
        "saturacao_base": saturacaoBase,
        "ctc_ph7": ctcpH7,
    }

    array_dados.append(dados)

    lista_registros.append(dados)

    novo_json_string = json.dumps(lista_registros)

    page.client_storage.set("dados_calagem",novo_json_string)

    criarTabela(e,array_dados,conteudo_tabela,page)
    limparCampos(amostra,saturacao_base,ctc_ph7)

    #print("Valores salvos:", dados)
    #print(array_dados)


def criarTabela(e,array_dados,conteudo_tabela,page):

    lista = ft.ListTile(
                leading=ft.Icon(ft.Icons.ALBUM),
                title=ft.Text(value=f'Amostra: {array_dados[-1]['amostra']}  Saturação por Base: {array_dados[-1]['saturacao_base']}  CTC pH7: {array_dados[-1]['ctc_ph7']}',color=ft.Colors.BLACK),
                trailing=ft.PopupMenuButton(
                    icon=ft.Icons.MORE_VERT,
                    items=[
                        ft.PopupMenuItem(text="Excluir",on_click=lambda e: excluirAmostra(e,lista,conteudo_tabela)),
                        ft.PopupMenuItem(text="Salvar",on_click=lambda e: salvarAmostra(e,page,array_dados)),
                    ],
                ),
            )
    
    conteudo_tabela.controls.append(lista)


def excluirAmostra(e,lista,conteudo_tabela):

    conteudo_tabela.controls.remove(lista)
    conteudo_tabela.update()


def salvarAmostra(e,page,dado):

    """Salva os dados localmente no client_storage"""
    dados_str = page.client_storage.get("amostraSalvas")

    # Se já existe, carrega a lista
    if dados_str:
        dados_lista = json.loads(dados_str)
    else:
        dados_lista = []

    # Adiciona o novo registro
    dados_lista.append(dado)

    # Salva novamente
    page.client_storage.set("amostraSalvas", json.dumps(dados_lista))
   

def limparCampos(amostra,saturacao_base,ctc_ph7):

    for campo in [amostra, saturacao_base, ctc_ph7]:
        campo.value = ""
        campo.update()


        