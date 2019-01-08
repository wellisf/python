'''
Exercício 5 - Vogais

Escreva a função vogal que recebe um único caractere como parâmetro
e retorna True se ele for uma vogal
e False se for uma consoante.

Note que

vogal("a") deve retornar True

vogal("b") deve retornar False

vogal("E") deve retornar True

Os valores True e False retornados devem ser do tipo bool (booleanos)
'''

from array import *

vowel = ['A','E','O','I','U']


def vogal(letter):

    i = 0
    control = False

    for i in range(5) :

        if(letter.upper() == vowel[i]) :
            control = True
            break

    return control

temp = (input('Digite uma letra '))

letter = temp[0]

print (vogal(letter))
