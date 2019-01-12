'''
(CESPE – 2017 – TRE/BA – Analista Judiciário – Analista de Sistemas) 

Assinale a opção que apresenta a saída resultante da execução do algoritmo antecedente.

a)123456
b)12121
c)12345
d)0112
e)12358
'''

a = 0
b = 1
f = 1

for x in range(2,7) :
	
	f = a + b
	a = b 
	b =f

	print(b) 
