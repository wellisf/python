'''

Retângulos 2

Refaça o exercício 1 imprimindo os retângulos sem preenchimento,
de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.

Por exemplo:

digite a largura: 10
digite a altura: 3

##########
#        #
##########

digite a largura: 2
digite a altura: 2

##
##

altura = 5
linha = 1

while linha <= altura:
    print("*", end = "")
    coluna = 2
    while coluna < altura: 
        if linha == 1 or linha == altura:
            print("*")
        else:
            print(end = " ")
        coluna = coluna + 1
    print("*")
    linha = linha + 1

'''

def retangulo(width, heigh):
	
	i = 0
	j = 0

	for j in range(heigh):
		
		for i in range(width):

			if ((j == 0) or (j == heigh-1)):
				print('#', end = "")	
			else :
				if ( i == 0) :
					print(end = '#')
				else :
					if (i == width -1):
						print(end = '#')
					else :
						print(end = ' ')
		print()


width = int(input('digite a largura: '))
heigh = int(input('digite a altura: '))

retangulo(width, heigh)

