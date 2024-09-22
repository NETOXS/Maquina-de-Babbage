import armazem

#iniciar o moinho com seus valores iniciais
def iniciar_moinho():
    global valores, resultado
    valores = []  
    resultado = 0

'''
função de zerar o moinho, para ser usada após o resultado da operação aritmética ser amazenado no armazám, assim o moinho é zerado, e caso,
dentro da entrada, o programador tenha inserido outras operações aritméticas com novos valores para serem realizadas, além da que já foi feita,
ela também possa ser processada sem ocorrer erros
'''
def zerar_moinho():
    global valores, resultado
    valores = []  
    resultado = 0

#carregar um operando do armazem, usando a função carregar_valor do armazem
def loadop(endereco):
    global valores
    valores.append(armazem.carregar_valor(endereco))

#armazenar o resultado da soma
def armazenar_resultado(endereco):
    global valores
    armazem.armazenar_valor(endereco, valores[2])

#funções aritmeticas
def soma():
    global resultado
    resultado = valores[0] + valores[1]
    valores.append(resultado)

def subtracao():
    global resultado
    resultado = valores[0] - valores[1]
    valores.append(resultado)

def multiplicacao():
    global resultado
    resultado = valores[0] * valores[1]
    valores.append(resultado)
