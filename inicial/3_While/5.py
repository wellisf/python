# -*- coding: utf-8 -*-

'''
Escreva um programa que receba um número inteiro positivo na entrada
e verifique se é primo.
Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

Exemplos:

Digite um número inteiro: 11

primo

Digite um número inteiro: 12

não primo
'''

def cousin(number):
    if(((number%2 == 0) or (number%3 == 0) or (number%5 == 0)) and ((number != 2) and (number != 3) and (number != 5))) :
        return False
    else :
        return True

number = int(input('Digite um número inteiro:'))

if(cousin(number)) :
    print('primo')
else :
    print('não primo')