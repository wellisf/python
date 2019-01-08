#Jogo NIM 
print("Bem-vindo ao jogo NIM!: Escolha entre as 2 opções: \n1 - para jogar uma partida isolada.\n2 - para jogar um campeonato.")

def computador_escolhe_jogada(n, m):
    #print('Computador joga')
    n = n - m
    #print(n)
    print('\nComputador retirou ', m, 'peça(s) do jogo, restam ', n)
    return n
    
def usuario_escolhe_jogada(n, m):
    #print('usuário joga')
    j = int(input('Entre com o valor de peças que vai eliminar: '))
    #j = 0
    if (j != m):
        j = int(input('Entre com o valor de peças que vai eliminar: '))
    else:
        n = n - j
        print('\nVocê retirou', j , ' ainda restam, ' , n, 'peça(s) em jogo.')
    return n

#Atribuindo os valores da partida
def partida():
    rodadaTeste = entradaDados()
    
    
    if (rodadaTeste == 1):
        rodadaMaximo = 1
        print('\nSeja bem vindo ao modo de partida isolada: ')
    else:
        rodadaMaximo = 3
        print('\nBem vindo ao modo Campeonato: ')
    
    rodada = 1
    computador = 0
    jogador = 0

    while (rodada <= rodadaMaximo):
        print('\nRodada: ', rodada)
        print("Entre apenas com valores numéricos maiores que 0: ")
        n = int(input('Quantas peças tem no jogo? '))
        m = int(input("Qual é o limite de peças por jogada? "))
        

        if(n > m and m > 0): #Verificando se a partida pode começar
            
            while (n > 0):
            #Verificando quem vai jogar
                jogada = n % (m + 1) == 0
                if (jogada == True):
                    n = usuario_escolhe_jogada(n, m)
                    #n = n - j
                    if (n <= 0):
                        print('\nJogador vence')
                        rodada += 1
                        jogador += 1
                        if(jogador > computador and rodada > 3):
                            print('\nJogador venceu por ', jogador, ' a ', computador)
                
                else:
                    #retorna true então o computador vai jogar
                    n = computador_escolhe_jogada(n, m)
                    #n = n - m
                    #print('\nComputador retirou ', m, 'peça(s) do jogo, restam ', n)
                    if (n <= 0):
                        print('\nComputador vence')
                        rodada += 1
                        computador += 1
                        if (computador > jogador and rodada > 3):
                            print('\nComputador venceu por ', computador, ' a ', jogador)
                
#Modificado a ordem de início do programa, para começar a ler a função partida, depois ler a entrada de dados.
def entradaDados():
    entrada = int(input('Valor: '))
    if (entrada < 1 or entrada > 2):
        print('\nNão existe esta opção, digite novamente a opção correta desejada: ')
        entradaDados() #Recursividade
        
    else:
        if(entrada == 1):
            return entrada
        else:
            return entrada
entrada = partida();