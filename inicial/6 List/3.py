'''

Maior elemento de uma lista

Escreva a função maior_elemento que recebe como parâmetro 
uma lista com números inteiros 
e devolve um número inteiro correspondente 
ao maior valor presente na lista recebida.

'''

#number = [7,8,9,15,1,2]

def maior_elemento(list):

	bigger = list[0]

	for x in range(1,len(list)):

		if bigger < list[x] :
			bigger = list[x]

	return bigger


#print(maior_elemento(number))