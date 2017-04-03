'''
Exercício 2 - Máximo

Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.

Note que

maximo(3,4) deve retornar 4

maximo(0,-1) deve retornar 0
'''

def bigger( one, two):

    if (one >= two ) :

        return one

    else :
        return two

numberOne = int(input('Digite um número '))
numberTwo = int(input('Digite outro número '))

print(bigger(numberOne, numberTwo))
