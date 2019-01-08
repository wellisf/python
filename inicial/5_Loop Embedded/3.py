'''

 Primos

Escreva a função n_primos que recebe um número inteiro
maior ou igual a 2 como parâmetro
e devolve
a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).

'''

def cousin(number):

    if (
    ((number%2 == 0) or (number%3 == 0) or (number%5 == 0))
    and not
    ((number == 3) or (number == 2) or (number == 5))
    ) :
        return False
    else :
        return True

def n_primos(number) :

	sum = 0

	while (1 < number ) :

		if( cousin(number) ) :

			sum = sum + 1

		number = number - 1

	return sum


number = int (input('Digite um número '))

print( n_primos(number) )