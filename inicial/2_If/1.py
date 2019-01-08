# -*- coding: utf-8 -*-

'''
programa deve receber os parâmetros a, b, e c da equação ax2+bx+c, respectivamente,
e imprimir o resultado na saída da seguinte maneira:

Quando não houver raízes reais imprima:

esta equação não possui raízes reais

Quando houver apenas uma raiz real imprima:

a raiz desta equação é X

onde X é o valor da raiz

Quando houver duas raízes reais imprima:

as raízes da equação são X e Y

onde X e Y são os valor das raízes.

Além disso, no caso de existirem 2 raízes reais, elas devem ser impressas em ordem crescente,
ou seja, X deve ser menor ou igual a Y.
'''

a = int(input('Informe o valor de A '))
b = int(input('Informe o valor de B '))
c = int(input('Informe o valor de C '))


complexo = False

delta = b*b - 4*a*c

if(delta == 0) :
    x1 = -b / (2*a)
    x2 = x1
elif(delta > 0) :
    x1 = (-b + (delta)**0.5)/(2*a)
    x2 = (-b - (delta)**0.5)/(2*a)
else :
    complexo = True

if (complexo) :
    print('esta equação não possui raízes reais')
elif(x1 == x2) :
    print('a raiz desta equação é',int(x1))
elif(x1 < x2) :
    print('as raízes da equação são',int(x1),'e', int(x2))
else :
    print('as raízes da equação são',int(x2),'e', int(x1))
