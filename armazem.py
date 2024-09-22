#iniciar o armazem com os valores nos endereços zerados
def iniciar_armazem():
    global lista_armazem
    lista_armazem = [0] * 16

#função de armazenar valor em um endereço do armazem
def armazenar_valor(endereco,valor):
    lista_armazem[endereco] = valor
    
#carregar algum valor do armazem no endereço especificado
def carregar_valor(endereco):
    return lista_armazem[endereco]