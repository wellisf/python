'''

Imprimindo matrizes

Como proposto na primeira vídeo-aula da semana, 
escreva uma função imprime_matriz(matriz), 
que recebe uma matriz como parâmetro e imprime a matriz, 
linha por linha. 

Note que NÃO se deve imprimir espaços após o último elemento de cada linha!

Exemplos:

minha_matriz = [[1], [2], [3]]
imprime_matriz(minha_matriz)
1
2
3


minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)
1 2 3
4 5 6

'''
minha_matriz = [[1, 2, 3], [4, 5, 6]]


def imprime_matriz(minha_matriz):
	
	line = len(minha_matriz)
	colunm = len(minha_matriz[0])

	for i in range(line):
		for j in range(colunm):
			
			if (j != (colunm-1)) :
				print(minha_matriz[i][j],end=' ')
			else : 
				print(minha_matriz[i][j])
		
		

	#print(minha_matriz[:])

imprime_matriz(minha_matriz)
