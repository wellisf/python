# -*- coding: utf-8 -*-

'''
Faça um programa em Python que receba quatro notas, calcule e imprima a média aritmética. Observe o exemplo abaixo:

Exemplo:

Entrada de Dados:
Digite a primeira nota: 4

Digite a segunda nota: 5

Digite a terceira nota: 6

Digite a quarta nota: 7

Saída de Dados:
A média aritmética é 5.5
'''
def media(p0,p1,p2,p3):
    return ((p0+p1+p2+p3)/4)

p0 = float(input('Digite a primeira nota:'))
p1 = float(input('Digite a segunda nota:'))
p2 = float(input('Digite a terceira nota:'))
p3 = float(input('Digite a quarta nota:'))

print ('A média aritmética é', media(p0,p1,p2,p3))
