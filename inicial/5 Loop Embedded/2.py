'''

Soma das hipotenusas

Escreva uma função 'soma_hipotenusas'
que receba como parâmetro um número inteiro positivo
e retorna a soma de todos os inteiros entre 1 e n
que são comprimento da hipotenusa de algum triângulo retângulo com catetos inteiros.

Atenção: um mesmo número pode ser hipotenusa de vários triângulos,
mas deve ser somado apenas uma vez.
Uma boa solução para este exercício
é fazer um laço de 1 até n testando
se o número é hipotenusa de algum triângulo.
Uma solução que dificilmente vai dar certo
é fazer um laço construindo triângulos
e somando as hipotenusas inteiras encontradas.



O resultado dos testes com seu programa foi:

***** [0.25 pontos]: Soma de hipotenusas ate 6 - Falhou *****
AssertionError: Expected 5 but got 21

***** [0.25 pontos]: Soma de hipotenusas ate 15 - Falhou *****
AssertionError: Expected 43 but got 120

***** [0.25 pontos]: Soma de hipotenusas ate 20 - Falhou *****
AssertionError: Expected 80 but got 210

***** [0.25 pontos]: Soma de hipotenusas ate 27 - Falhou *****
AssertionError: Expected 131 but got 378

'''

'''
def hipotenusa(a,b,c):
	
	if (a**2 == b**2 + c**2 ) :
		return True
	else :
		return False

def soma_hipotenusas(number):

	sum = 0

	switch = True

	d = number*2


	for i in range(1,number+1):

		a = 1
		b = 1

		for j in range(1,d):

			if(j != 1) :

				if (switch):
					a = a + 1
					switch = False

				else :
					b = b + 1
					#print(b)
					switch = True

			if ( hipotenusa(i,b,a) ):
				#print(i,b,a)
				sum = sum + i
		
	return sum

number = int(input('digite um número inteiro positivo '))

print (soma_hipotenusas(number))
'''

def calcular_hipotenusa(a, b):
    return ((a*a) + (b*b))
 
def soma_hipotenusas(n):
    c = 1
    soma = 0
    while (c <= n):
        _c = (c*c)      
        a = 1
        b = 1
        while (a < n):
            while (b < n):
                if (_c == calcular_hipotenusa(a, b)):
                    #print(a, " - " ,b , " - " , c)
                    soma = soma + c
                    a = n
                    break
                b += 1
            a += 1
            b = a
        c += 1
   
    return soma

number = int(input('digite um número inteiro positivo '))

soma_hipotenusas(number)

print (soma_hipotenusas(number))