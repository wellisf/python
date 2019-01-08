# -*- coding: utf-8 -*-

'''

Receba um número inteiro positivo na entrada
e imprima os n primeiros números ímpares naturais.
Para a saída, siga o formato do exemplo abaixo.

Exemplo:

Digite o valor de n: 5
1
3
5
7
9
'''

def odd(number):

    if(number%2 == 0) :
        return False
    else :
        return True

number = int(input('Digite o valor de n: '))

if odd(number) :

    i = 0
    temp = number-(number-1)

    for i in range(number) :
        print(temp)
        temp = temp + 2
else :

    i = 0
    temp = number-(number-1)

    for i in range(number) :

        '''if(temp+1 == number) :
            print(temp)
            print(number)
            #control = False
            temp = temp + 2
        else : '''
        print(temp)
        temp = temp + 2
