import armazem

#imprimir o que foi requisitado nas instruções
#coloquei a saída como 016b ao inves de 08b, pois no exemplo de saída no pdf esta em 016b!
def imprimir(endereco, saida):
    valor = armazem.carregar_valor(endereco)
    impressao = format(valor, '016b').replace('1', 'X').replace('0', 'O') 
    with open(saida, 'a') as saida:
        saida.write(f"{impressao[:4]} {impressao[4:8]} {impressao[8:12]} {impressao[12:16]}\n")
        saida.close()