'''  
(IADES - 2011 – TRE- Programador de Computador)

Dado o algoritmo escrito em pseudocódigo, quais os valores de N1 e N2,
respectivamente, ao final da execução?
a) 162 e 110.
b) 110 e 121.
c) 110 e 162.
d) 121 e 110.
e) 173 e 110.
'''

n1 = 2
n2 = 30

while n1 < n2:
  n2 += n1
  n1 *= 3

n1 += 11

print('N1 is equal: ',n1)
print('N2 is equal: ',n2)
