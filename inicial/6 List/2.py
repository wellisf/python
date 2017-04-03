'''

Soma dos elementos de uma lista

Como vimos, uma função pode receber parâmetros. 
mas listas também podem ser passadas como parâmetros para funções. 
Neste exercício você vai fazer exatamente isso: 
escreva a função soma_elementos que recebe como parâmetro 
uma lista com números inteiros 
e devolve um número inteiro correspondente à soma dos elementos da lista recebida.


'''

#number = [7,8,9,15,1,2]

def soma_elementos(list):

	sum = 0

	for x in range(0,len(list)):
		
		sum = sum + list[x]

	return sum


#print(soma_elementos(number))


