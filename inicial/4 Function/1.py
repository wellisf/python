'''
Exercício 1 - FizzBuzz

Escreva a função fizzbuzz que recebe como parâmetro um número inteiro
e retorna

'Fizz' se o número for divisível por 3 e não for divisível por 5;

'Buzz' se o número for divisível por 5 e não for divisível por 3;

'FizzBuzz' se o número for divisível por 3 e por 5;

Caso a função não seja divisível 3 e também não seja divisível por 5,
ela deve retornar o número recebido como parâmetro.

Note que

fizzbuzz(3) deve retornar Fizz

fizzbuzz(5) deve retornar Buzz

fizzbuzz(15) deve retornar FizzBuzz

fizzbuzz(4) deve retornar 4

As cadeias de caracteres Fizz e Buzz devem respeitar letras maiúsculas e minúsculas
'''


def fizzbuzz(number):

    if((number%5 == 0) and (number%3 == 0)) :

        return 'FizzBuzz'

    elif(number%5 == 0) :

        return 'Buzz'

    elif (number%3 == 0) :

        return 'Fizz'

    else :

        return number

n = int(input('Digite um número '))

print(fizzbuzz(n))