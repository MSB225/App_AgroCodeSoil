
# Funções.py

def interpretar_ph_agua(input1, dados_laudo):
    try:
        # Tenta converter input1 para float
        input1_float = float(input1)

        if input1_float <= 5:
            dados_laudo['pH_água'].append('Muito Baixo')

        elif 5.1 <= input1_float <= 5.4:
            dados_laudo['pH_água'].append('Baixo')

        elif 5.5 <= input1_float <= 6.0:
            dados_laudo['pH_água'].append('Médio')

        else:
            dados_laudo['pH_água'].append('Alto')

    except ValueError:
        return "Por favor, insira um valor numérico válido para o pH."

    return dados_laudo


def interpretar_saturação_por_bases(input2,dados_laudo):
    
    try:
        # Tenta converter input1 para float
        input2_float = float(input2)

        if input2_float < 45:
            dados_laudo['Saturação_por_bases'].append('Muito Baixo')

        elif 45 <= input2_float <= 64:
            dados_laudo['Saturação_por_bases'].append('Baixo')

        elif 65 <= input2_float <= 80:
            dados_laudo['Saturação_por_bases'].append('Médio')

        else:
            dados_laudo['Saturação_por_bases'].append('Alto')

    except ValueError:
        return "Por favor, insira um valor numérico válido para o pH."

    return dados_laudo

def interpretar_saturação_por_alumínio(input3,dados_laudo):
    
    try:
        # Tenta converter input1 para float
        input3_float = float(input3)

        if input3_float < 1:
            dados_laudo['Saturação_por_alumínio'].append('Muito Baixo')

        elif 1 <= input3_float <= 10:
            dados_laudo['Saturação_por_alumínio'].append('Baixo')

        elif 10.1 <= input3_float <= 20:
            dados_laudo['Saturação_por_alumínio'].append('Médio')

        else:
            dados_laudo['Saturação_por_alumínio'].append('Alto')

    except ValueError:
        return "Por favor, insira um valor numérico válido para o pH."

    return dados_laudo


def interpretar_argila(input4,dados_laudo):
    try:
        # Tenta converter input1 para float
        input4_float = float(input4)

        if input4_float <= 20:
            dados_laudo['Argila'].append('4')

        elif 21 <= input4_float <= 40:
            dados_laudo['Argila'].append('3')

        elif 41 <= input4_float <= 60:
            dados_laudo['Argila'].append('2')

        else:
            dados_laudo['Argila'].append('1')

    except ValueError:
        return "Por favor, insira um valor numérico válido para o pH."

    return dados_laudo

def interpretar_matéria_orgânica(input5,dados_laudo):
    try:
        # Tenta converter input1 para float
        input5_float = float(input5)

        if input5_float <= 2.5:
            dados_laudo['Matéria_orgânica'].append('Baixo')

        elif 2.6 <= input5_float <= 5.0:
            dados_laudo['Matéria_orgânica'].append('Médio')

        elif input5_float > 5.0:
            dados_laudo['Matéria_orgânica'].append('Alto')

        else:
            dados_laudo['Matéria_orgânica'].append('--')

    except ValueError:
        return "Por favor, insira um valor numérico válido para o pH."

    return dados_laudo


def interpretar_ctc_ph7(input6,dados_laudo):
    
    try:
        # Tenta converter input1 para float
        input6_float = float(input6)

        if input6_float <= 5.0:
            dados_laudo['CTC_pH7'].append('Baixo')

        elif 5.1 <= input6_float <= 15.0:
            dados_laudo['CTC_pH7'].append('Médio')

        elif input6_float > 15.0:
            dados_laudo['CTC_pH7'].append('Alto')

        else:
            dados_laudo['CTC_pH7'].append('--')

    except ValueError:
        return "Por favor, insira um valor numérico válido para o pH."

    return dados_laudo


def interpretar_fosforo(input7, dados_laudo):
    try:
        # Tenta converter input7 para float
        input7_float = float(input7)

        # Verifica o último valor de Argila adicionado
        argila = dados_laudo['Argila'][-1]  # Acessa o último valor de 'Argila'

        if argila == '1':

            if input7_float <= 2.0:
                dados_laudo['Fósforo'].append('Muito baixo')
            elif 2.1 <= input7_float <= 4.0:
                dados_laudo['Fósforo'].append('Baixo')
            elif 4.1 <= input7_float <= 6.0:
                dados_laudo['Fósforo'].append('Médio')
            elif 6.1 <= input7_float <= 12.0:
                dados_laudo['Fósforo'].append('Alto')
            else:
                dados_laudo['Fósforo'].append('Muito Alto')

        elif argila == '2':

            if input7_float <= 3.0:
                dados_laudo['Fósforo'].append('Muito baixo')
            elif 3.1 <= input7_float <= 6.0:
                dados_laudo['Fósforo'].append('Baixo')
            elif 6.1 <= input7_float <= 9.0:
                dados_laudo['Fósforo'].append('Médio')
            elif 9.1 <= input7_float <= 18.0:
                dados_laudo['Fósforo'].append('Alto')
            else:
                dados_laudo['Fósforo'].append('Muito Alto')

        elif argila == '3':

            if input7_float <= 4.0:
                dados_laudo['Fósforo'].append('Muito baixo')
            elif 4.1 <= input7_float <= 8.0:
                dados_laudo['Fósforo'].append('Baixo')
            elif 8.1 <= input7_float <= 12.0:
                dados_laudo['Fósforo'].append('Médio')
            elif 12.1 <= input7_float <= 24.0:
                dados_laudo['Fósforo'].append('Alto')
            else:
                dados_laudo['Fósforo'].append('Muito Alto')

        elif argila == '4':
            
            if input7_float <= 7.0:
                dados_laudo['Fósforo'].append('Muito baixo')
            elif 7.1 <= input7_float <= 14.0:
                dados_laudo['Fósforo'].append('Baixo')
            elif 14.1 <= input7_float <= 21.0:
                dados_laudo['Fósforo'].append('Médio')
            elif 21.1 <= input7_float <= 42.0:
                dados_laudo['Fósforo'].append('Alto')
            else:
                dados_laudo['Fósforo'].append('Muito Alto')

    except ValueError:
        return "Por favor, insira um valor numérico válido para Fósforo."

    return dados_laudo


def interpretar_potássio(input8, dados_laudo):
    try:
        input8_float = float(input8)
        ctc_classificacao = dados_laudo['CTC_pH7'][-1]  # Pega o último valor adicionado à lista

        # Define os intervalos para cada classificação de CTC
        if ctc_classificacao == 'Baixo':
            if input8_float <= 15:
                dados_laudo['Potássio'].append('Muito baixo')
            elif 16 <= input8_float <= 30:
                dados_laudo['Potássio'].append('Baixo')
            elif 31 <= input8_float <= 45:
                dados_laudo['Potássio'].append('Médio')
            elif 46 <= input8_float <= 90:
                dados_laudo['Potássio'].append('Alto')
            else:
                dados_laudo['Potássio'].append('Muito Alto')

        elif ctc_classificacao == 'Médio':
            if input8_float <= 20:
                dados_laudo['Potássio'].append('Muito baixo')
            elif 21 <= input8_float <= 40:
                dados_laudo['Potássio'].append('Baixo')
            elif 41 <= input8_float <= 60:
                dados_laudo['Potássio'].append('Médio')
            elif 61 <= input8_float <= 120:
                dados_laudo['Potássio'].append('Alto')
            else:
                dados_laudo['Potássio'].append('Muito Alto')

        elif ctc_classificacao == 'Alto':
            if input8_float <= 30:
                dados_laudo['Potássio'].append('Muito baixo')
            elif 31 <= input8_float <= 60:
                dados_laudo['Potássio'].append('Baixo')
            elif 61 <= input8_float <= 90:
                dados_laudo['Potássio'].append('Médio')
            elif 91 <= input8_float <= 180:
                dados_laudo['Potássio'].append('Alto')
            else:
                dados_laudo['Potássio'].append('Muito Alto')

    except ValueError:
        return "Por favor, insira um valor numérico válido para o potássio."

    return dados_laudo

