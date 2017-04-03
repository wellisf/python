'''
Exercício 3 - Primos

Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro
e retorna o maior número primo menor ou igual ao número passado à função

Note que

maior_primo(100) deve retornar 97

maior_primo(7) deve retornar 7

'''

def cousin(number):

    if (
    ((number%2 == 0) or (number%3 == 0) or (number%5 == 0))
    and not
    ((number == 3) or (number == 2) or (number == 5))
    ) :
        return False
    else :
        return True

def maior_primo(number) :

    while (1 < number ) :

        if ( cousin(number) ) :
            return number
            break

        number = number - 1




number = int (input('Digite um número '))

print(maior_primo(number))
