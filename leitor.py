#ler as instruções do arquivo
def ler_instrucao(entrada):
    instrucoes = []
    with open(entrada, 'r') as entrada:
        for linha in entrada:
            linha = linha.replace('X', '1').replace('O', '0').replace(' ', '')  
            instrucoes.append((linha[:4], linha[4:8], linha[8:16]))
    return instrucoes
