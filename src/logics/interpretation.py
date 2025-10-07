
resultado_amostra={}

def interpretarSaturacaoBase(saturacao_base,resultado_amostra):
    
    try:
        # Tenta converter input1 para float
        input1_float = float(saturacao_base.value)
        print(input1_float)

        if input1_float < 45:
            
            condicao="Muito Baixo"
            resultado_amostra["SaturacaoBase"]=condicao

        elif 45 <= input1_float <= 64:
            
            condicao="Baixo"
            resultado_amostra["SaturacaoBase"]=condicao

        elif 65 <= input1_float <= 80:
           
            condicao="Médio"
            resultado_amostra["SaturacaoBase"]=condicao

        elif input1_float > 80:

            condicao="Alto"
            resultado_amostra["SaturacaoBase"]=condicao

        else:

            condicao="--"
            resultado_amostra["SaturacaoBase"]=condicao

    except ValueError:
        return "Por favor, insira um valor numérico válido para o pH."


def interpretarCTC_pH7(ctc_ph7,resultado_amostra):
    
    try:
        # Tenta converter input1 para float
        input6_float = float(ctc_ph7.value)
        print(input6_float)

        if input6_float <= 5.0:
            
            condicao = "Baixo"
            resultado_amostra["CTCpH7"]= condicao

        elif 5.1 <= input6_float <= 15.0:
            
            condicao = "Médio"
            resultado_amostra["CTCpH7"]= condicao

        elif input6_float > 15.0:
            
            condicao = "Alto"
            resultado_amostra["CTCpH7"]= condicao

        else:

            condicao = "--"
            resultado_amostra["CTCpH7"]= condicao
        

    except ValueError:
        return "Por favor, insira um valor numérico válido para o pH."

    

print(resultado_amostra)