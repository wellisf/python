# -*- coding: utf-8 -*-

'''
Escreva um programa que receba um número natural n na entrada
e imprima n! (fatorial) na saída.

Exemplo:

Digite o valor de n: 5
120

'''

def fatorial(number):

    temp = 1

    while (1 < number) :
        temp = number * temp
        number -= 1

    return temp

number = int(input('Digite o valor de n: '))

print(fatorial(number))