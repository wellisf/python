'''
Exercício 4 - Máximo com 3 parâmetros

Reescreva a função 'maximo' do exercício 2,
que devolve o maior valor dentre dois inteiros recebidos,
para que ela passe a receber 3 valores inteiros como parâmetros
e devolva o maior dentre eles.

Note que

maximo(30,14,10) deve retornar 30

maximo(0,-1, 1) deve retornar 1

'''

def maximo( one, two, three):

    if (one >= two >= three ) :

        return one

    elif (three >= two ) :

        return three

    else :

        return two


numberOne = int(input('Digite um número '))
numberTwo = int(input('Digite outro número '))
numberThree = int(input('Digite mais um número '))

print(maximo(numberOne, numberTwo, numberThree))