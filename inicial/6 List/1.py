'''

Invertendo sequência


Como pedido na primeira video-aula desta semana, 
escreva um programa que recebe uma sequência de números inteiros 
terminados por 0 e imprima todos os valores em ordem inversa. 
Note que 0 (ZERO) não deve fazer parte da sequência.

Exemplo:

Digite um número: 1
Digite um número: 7
Digite um número: 4
Digite um número: 0

4
7
1

'''

number = []

start = True

while start:

	temp = (int(input('Digite um número: ')))

	if ( temp == 0) :
		break
	else :
		number.append(temp)

x = len(number) - 1

while x >= 0:

	if (number[x] != 0) :
		print(number[x])

	x = x - 1
	