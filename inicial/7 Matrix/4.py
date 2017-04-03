'''

Matrizes multiplicáveis

Duas matrizes são multiplicáveis 
se o número de colunas da primeira é igual ao número de linhas da segunda. 
Escreva a função sao_multiplicaveis(m1, m2) 
que recebe duas matrizes como parâmetro 

e devolve True se as matrizes forem multiplicavéis (na ordem dada) 
e False caso contrário.

Exemplos:

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
sao_multiplicaveis(m1, m2) => False


m1 = [[1], [2], [3]]
m2 = [[1, 2, 3]]
sao_multiplicaveis(m1, m2) => True

'''

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]

def sao_multiplicaveis(m1,m2):
	
	column = len(m1[0])
	line2 = len(m2)
	

	if (column == line2) :

		return True
	else :
	 
		return False
		

print(sao_multiplicaveis(m1,m2))