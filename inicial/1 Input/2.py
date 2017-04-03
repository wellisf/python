# -*- coding: utf-8 -*-

'''
Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado,
calcule e imprima (saída de dados) seu perímetro e sua área.

Observação: a saída deve estar no formato: "perímetro: x - área: y"

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

Entrada de Dados:
Digite o valor correspondente ao lado de um quadrado: 3

Saída de Dados:
perímetro: 12 - área: 9
'''
'''
def area(side):
    return (side**2)

def perimetro(side):
    return (side*4)
'''

side = int(input("Digite o valor correspondente ao lado de um quadrado: "))


#print('perímetro: ',perimetro(side),' - área: ',area(side))

print('perímetro: ', side*4,'- área: ',side**2)

#x = ('perímetro: '+str(perimetro(side))+' - área: '+str(area(side)))

#print('perímetro: ', p,'- área: ',a)

#print (x)

