# -*- coding: utf-8 -*-

'''
Distância entre dois pontos

Receba 4 números inteiros na entrada. Os dois primeiros devem corresponder,
respectivamente, às coordenadas x e y de um ponto em um plano cartesiano.
Os dois últimos devem corresponder, respectivamente,
às coordenadas x e y de um outro ponto no mesmo plano.

Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10,

imprima longe na saída.

Caso o contrário, quando a distância for menor que 10, imprima perto
'''

def distance(x1,y1,x2,y2) :
    d = ((x2-x1)**2 + (y2 - y1)**2)**0.5
    return d

xa = int(input('Informe a coordenadas x '))
ya = int(input('Informe a coordenadas y '))
xb = int(input('Informe a coordenadas x '))
yb = int(input('Informe a coordenadas y '))

if (distance(xa,ya,xb,yb) < 10 ) :
    print('Perto')
else :
    print('Longe')