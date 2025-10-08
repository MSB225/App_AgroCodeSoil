import flet as ft
import random
import json

from logics.interpretation import resultado_amostra,interpretarSaturacaoBase,interpretarCTC_pH7

lista_valores=[]
lista_amostras=[]
Id = random.randint(100000, 999999)

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
                on_click=lambda e: (interpretarSaturacaoBase(saturacao_base),interpretarCTC_pH7(ctc_ph7),guardarDados(e,Id,page,amostra,saturacao_base,ctc_ph7,conteudo_tabela),guardarValores(e,Id,page,amostra,saturacao_base,ctc_ph7,conteudo_tabela)),
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



def guardarDados(e,Id,page,amostra,saturacao_base,ctc_ph7,conteudo_tabela):

    dadosAmostra = page.client_storage.get("dadosAmostra") # lista_dados

    # Converte para a lista Python (array) ou inicializa como lista vazia
    if dadosAmostra:
        lista_registros_amostras = json.loads(dadosAmostra)
    else:
        # Se for a primeira vez, cria a lista vazia
        lista_registros_amostras = []

    amostraCalagem = amostra.value

    dados_amostra={

        "id": Id,
        "amostra": amostraCalagem,
        "saturacao_base": resultado_amostra["SaturacaoBase"],
        "ctc_ph7": resultado_amostra["CTCpH7"]

    }

    # salvar os dados amostra

    lista_amostras.append(dados_amostra)

    lista_registros_amostras.append(dados_amostra)

    novo_json_string_amostras = json.dumps(lista_registros_amostras)

    page.client_storage.set("dadosAmostra",novo_json_string_amostras)

    criarTabela(e,lista_amostras,conteudo_tabela,page)
    limparCampos(amostra,saturacao_base,ctc_ph7)
    

def guardarValores(e,Id,page,amostra,saturacao_base,ctc_ph7,conteudo_tabela):

    dadosValores = page.client_storage.get("dadosValores") # lista_valores

    # Converte para a lista Python (array) ou inicializa como lista vazia
    if dadosValores:
        lista_registros_valores = json.loads(dadosValores)
    else:
        # Se for a primeira vez, cria a lista vazia
        lista_registros_valores = []

    
    amostraCalagem = amostra.value
    saturacaoBase = saturacao_base.value
    ctcpH7 = ctc_ph7.value

    dados_valores = {

        "id": Id,
        "amostra": amostraCalagem,
        "saturacao_base": saturacaoBase,
        "ctc_ph7": ctcpH7,
    }

    # salvar os dados valores

    lista_valores.append(dados_valores)

    lista_registros_valores.append(dados_valores)

    novo_json_string_valores = json.dumps(lista_registros_valores)

    page.client_storage.set("dadosValores",novo_json_string_valores)


def criarTabela(e,array_dados,conteudo_tabela,page):

    dados_da_amostra = array_dados[-1]

    amostra_id = dados_da_amostra['id']

    lista = ft.ListTile(
                leading=ft.Icon(ft.Icons.ALBUM),
                title=ft.Text(value=f'Amostra: {dados_da_amostra['amostra']}  Saturação por Base: {dados_da_amostra['saturacao_base']}  CTC pH7: {dados_da_amostra['ctc_ph7']}',color=ft.Colors.BLACK),
                trailing=ft.PopupMenuButton(
                    icon=ft.Icons.MORE_VERT,
                    items=[
                        ft.PopupMenuItem(text="Excluir",on_click=lambda e: (excluirDadosAmostras(e,lista,conteudo_tabela,amostra_id,page),excluirDadosValores(e,conteudo_tabela, amostra_id, page))) ,
                        ft.PopupMenuItem(text="Salvar",on_click=lambda e: salvarAmostra(e,page,array_dados)),
                    ],
                ),
            )
    
    conteudo_tabela.controls.append(lista)


def excluirDadosAmostras(e, lista, conteudo_tabela, amostra_id, page):
    
    # 1. Obter a string JSON do client_storage
    json_string_salva_amostras = page.client_storage.get("dadosAmostra")

    if json_string_salva_amostras:
        # 2. Converte para a lista Python
        lista_registros_amostras = json.loads(json_string_salva_amostras)
        
        # 3. Filtrar a lista, removendo o objeto com o ID
        # Usamos uma 'list comprehension' ou 'filter' para criar uma nova lista
        # que inclui apenas os dicionários onde o 'id' NÃO é igual ao amostra_id.
        lista_atualizada_amostras = [
            registro for registro in lista_registros_amostras 
            if registro.get('id') != amostra_id
        ]

        # 4. Converte a lista atualizada de volta para string JSON
        novo_json_string_amostras = json.dumps(lista_atualizada_amostras)

        # 5. Gravar a nova string JSON no client_storage
        page.client_storage.set("dadosAmostra", novo_json_string_amostras)

    # 6. Remover o item visualmente da tabela
    conteudo_tabela.controls.remove(lista)
    
    # 7. Atualizar a UI do Flet
    conteudo_tabela.update()
    
    # Opcional: Atualizar a página inteira se a remoção for crítica
    # page.update() 

def excluirDadosValores(e,conteudo_tabela, amostra_id, page):

    # 1. Obter a string JSON do client_storage
    json_string_salva_valores = page.client_storage.get("dadosValores")

    if json_string_salva_valores:
        # 2. Converte para a lista Python
        lista_registros_valores = json.loads(json_string_salva_valores)
        
        # 3. Filtrar a lista, removendo o objeto com o ID
        # Usamos uma 'list comprehension' ou 'filter' para criar uma nova lista
        # que inclui apenas os dicionários onde o 'id' NÃO é igual ao amostra_id.
        lista_atualizada_valores = [
            registro for registro in lista_registros_valores 
            if registro.get('id') != amostra_id
        ]

        # 4. Converte a lista atualizada de volta para string JSON
        novo_json_string_valores = json.dumps(lista_atualizada_valores)

        # 5. Gravar a nova string JSON no client_storage
        page.client_storage.set("dadosValores", novo_json_string_valores)

 
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


        