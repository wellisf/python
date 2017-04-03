'''

Soma de matrizes

Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes 
e devolve uma matriz que represente sua soma 
caso as matrizes tenham dimensões iguais. 
Caso contrário, a função deve devolver False.

Exemplos:

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
soma_matrizes(m1, m2) => [[3, 5, 7], [9, 11, 13]]


m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]
soma_matrizes(m1, m2) => False

'''

m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]


def dimensões(m1,m2):
	
	line = len(m1)
	column = len(m1[0])

	line2 = len(m2)
	column2 = len(m2[0])

	if ( (line == line2) and (column2 == column) ) : 

		return True

	else :
		
		return False

def soma_matrizes(m1,m2):

	if (dimensões(m1,m2)):
		
		for i in range(len(m1)):
			for j in range(len(m1[0])):
				
				m1[i][j] = m1[i][j] + m2[i][j]

		return m1

	else: 
		return False

if ( (soma_matrizes(m1,m2)) == False ) :
	print('False')
else :
	print ( soma_matrizes(m1,m2)[:] )

