# @welcome()
# It works with welcome screen

def welcome():

    print('\nBem-vindo ao jogodo NIM! Escolha : \n')


# @menu()
# and menu selecting the type of departure of the user.
# Is return a boolean, being true for isolated start, and false for championship

def menu():

    option = int(input('1 - para jogar uma partida isolada \n2 - para jogar um campeonato  '))

    return (option == 1)
	
'''

que recebe, como parâmetros, 
os números n e m descritos acima 
e devolve um inteiro correspondente 
à próxima jogada do computador de acordo com a estratégia vencedora.

'''

#arrumar este trem, esta dano erro

def computador_escolhe_jogada(n,m):

    n = n - m
    print('\nComputador retirou ', m, 'peça(s) do jogo, restam ', n)
    return n


'''

que recebe os mesmos parâmetros, 
solicita que o jogador informe sua jogada 
e verifica se o valor informado é válido. 
Se o valor informado for válido, 
a função deve devolvê-lo; 
caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida.

'''


def usuario_escolhe_jogada(n,m):
	
	test = True

	while (test):
		
		played =  int (input('\nQuantas peças você vai tirar? '))

		if ((played <= m) and (n - played > 0) ):
			break
		else : 
			print('Oops! Jogada inválida! Tente de novo.')

	return played

'''

que não recebe nenhum parâmetro, 
solicita ao usuário que informe os valores de n e m 
e inicia o jogo, 
alternando entre jogadas do computador e do usuário 
(ou seja, chamadas às duas funções anteriores). 
A escolha da jogada inicial deve ser feita em função da estratégia vencedora, 
como dito anteriormente. 
A cada jogada, deve ser impresso na tela o estado atual do jogo, 
ou seja, quantas peças foram removidas na última jogada 
e quantas restam na mesa. Quando a última peça é removida, 
essa função imprime na tela 
a mensagem "O computador ganhou!" ou "Você ganhou!" conforme o caso.


'''
def partida(numberPerGame,maximumPerShift) :

	#actual = numberPerGame
	temp = 0
	turn = True
	
	while (numberPerGame != 0) :

		if (turn) :
			
			temp = usuario_escolhe_jogada(numberPerGame,maximumPerShift)
			numberPerGame = numberPerGame - temp 

			print("Você tirou",temp," peças")
			print("Agora resta apenas",numberPerGame," peça no tabuleiro.")

			if (numberPerGame == 1):
				print('Fim do jogo! Você ganhou!')
				return True
				break

			turn = False

		else :

			temp = computador_escolhe_jogada(numberPerGame,maximumPerShift)
			numberPerGame = numberPerGame - temp 

			print("O computador tirou",temp," peças")
			print("Agora resta apenas",numberPerGame," peça no tabuleiro.")

			if (numberPerGame == 1):
				print('Fim do jogo! O computador ganhou!')
				return False
				break

			turn = True


#---------------------------------------------------------------------------------
# ----------------------------------- CALLS --------------------------------------
#---------------------------------------------------------------------------------

welcome()

if ( menu() ) :

    print('\nVocê escolheu um partida isolada! ')

    n = 0
    m = 1

    while(n < m):
    	n = int(input('\nQuantas peças? '))
    	m = int(input('Limite de peças por jogada? '))

    if (partida(n,m)) :
    	print('voce ganhou')
    else :
    	print('o computador ganhou')

else :

	print('\nVocê escolheu um campeonato! ')

	computer = 0
	you = 0
	games  = 0 

	n = 0
	m = 1
	
	while(n < m):
		n = int(input('\nQuantas peças? '))
		m = int(input('Limite de peças por jogada? '))

	while (games < 3):
		
		if (partida(n,m)) :

			you = you + 1
			
		else :

			computer = computer + 1

		games = games + 1 

	print('Placar: Você',you,' X ',computer,' Computador')


