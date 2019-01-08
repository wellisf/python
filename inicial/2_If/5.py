# -*- coding: utf-8 -*-

'''
FizzBuzz parcial, parte 3

Receba um número inteiro na entrada e imprima

FizzBuzz na saída se o número for divisível por 3 e por 5.
Caso contrário, imprima o mesmo número que foi dado na entrada.
'''

def fizz(number):
    if((number%5 == 0) and (number%3 == 0)) :
        return True
    else :
        return False

number = int(input('Informe um numero '))

if(fizz(number)) :
    print('FizzBuzz')
else :
    print(number)