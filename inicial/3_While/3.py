# -*- coding: utf-8 -*-

'''
Escreva um programa que receba um número inteiro na entrada,
calcule e imprima a soma dos dígitos deste número na saída

Exemplo:

Digite um número inteiro: 123
6

'''

# soma a unidade com dezena com centena e assim por diante

def autoSum(number):

    sum = 0

    count = 0

    count = len(str(number))

    temp = str(number)
    #print('ala')
    #print(temp[0])
    a = 0

    while ( count > a) :
        #print(temp[a])
        sum = int(temp[a]) + sum
        a = a + 1

    return sum

number = int(input('Digite um número inteiro:'))

print(autoSum(number))
