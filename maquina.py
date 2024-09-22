#Desenvolvido por: José Portela da Silva Neto e Kaynan Andrey Hermano Siqueira

'''
ATENÇÃO PROFESSOR: não compreendi perfeitamente no pdf quando informa que o progamador que escolhe os nomes dos arquivos de entrada e saída, 
mas logo após diz que a entrada e saída tem por parâmetros padrões "cartao.in" e "cartao.out". Então não compreendi como deve ser feito essa parte,
daí coloquei como parâmetro padrão na função, fui tirar essa dúvida na quarta-feira mas soube que não ia haver o encontro no laboratório, também encaminhei
um email para o senhor sobre a dúvida. Também soube que o senhor irá inserir um arquivo que apenas irá puxar as funções da máquina para executar, então não
inseri as funções ligar_maquina e configurar param serem iniciadas no módulo máquina.  
'''
import leitor, moinho, armazem, impressora

#configurar a maquina de babbage com a entrada e saida padrão, alem de inicializar o moinho e o armazem 
def configurar(nome_arquivo_entrada = 'cartao.in', nome_arquivo_saida = 'cartao.out'):
    global entrada, saida 
    entrada = nome_arquivo_entrada
    saida = nome_arquivo_saida
    moinho.iniciar_moinho()
    armazem.iniciar_armazem()

#realizar as instruções lidas no leitor
def ligar_maquina():
    instrucoes = leitor.ler_instrucao(entrada)
    for instrucao in instrucoes:
        operacao = instrucao[0]
        endereco = int(instrucao[1],2)
        valor = int(instrucao[2],2)

        #storeim - armazena um valor no armazem
        if operacao == '0001': 
            armazem.armazenar_valor(endereco, valor)
        #loadop - carrega um valor endereçado no armazem como um operando do moinho para realizar uma operação
        elif operacao == '0010':
            moinho.loadop(endereco)
        #opreração de soma
        elif operacao == "0011":
            moinho.soma()
        #opreração de subtração
        elif operacao == "0100":
            moinho.subtracao()
        #opreração de multiplicação
        elif operacao == "0101":
            moinho.multiplicacao()
        #store - armazena o resultado da operação feita no moinho
        elif operacao == '0110':
            moinho.armazenar_resultado(endereco)
            moinho.zerar_moinho()
        #print - imprime o valor endereçado no armazem no cartão de saida
        elif operacao == '0111':
            impressora.imprimir(endereco, saida)
