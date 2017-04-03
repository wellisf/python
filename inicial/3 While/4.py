# -*- coding: utf-8 -*-

'''
Exercício 4 - Desafio do vídeo "Repetição com while":

Escreva um programa que receba um número inteiro na entrada
e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele.
Caso exista, imprima "sim". Se não existir, imprima "não".

Exemplos:

Digite um número inteiro: 123
não
Digite um número inteiro: 3556
sim

'''

def numberIgual(number):

    count  = len(number)

    i = 0
    control = False

    for i in range(count - 1) :
        #print(number[i])

        j = i + 1

        while (j < count) :
            #print(j)

            if ( number[i] == number[j]) :
                control = True
                break

            j = j + 1

    return control

def adjacent(number):

    c = len(number)

    if (c == 1)  :

        return False
    elif (c == 2) :

        if (number[0] == number[1]) :

            return True
        else :

            return False
    else :

        control = False
        i = 1

        while (i < (c-1)) :

            #print (number[i])

            if ((number[i] == number[i+1]) or (number[i] == number[i-1])) :

                control = True
                break

            i = i + 1

        return control




number = input('Digite um número inteiro: ')

if (adjacent(number)) :
    print('Sim')
else :
    print('Não')











'''
entradaUsuario = input("Entre com o número que deseja verificar se tem caractere adjacente igual: ")
tamanho = len(entradaUsuario) #Coleta a quantidade de caractere e armazena na variável
tempEntrada = int(entradaUsuario) #converte o valor de entrada de string para número inteiro
ultimoNumero = 0
saoIguais = False
paraLoop = 0 #Serve de controle para o looping

while (tamanho > paraLoop and not saoIguais):
    ultimoNumero = tempEntrada % 10 #variável que vai receber apenas o último caractere da string passada pelo usuário
    tempEntrada = tempEntrada // 10 #atualizando o valor de entrada, retirando apenas o último caractere, já que o mesmo está armazenado na varipável "teste"

    if(tempEntrada % 10 != ultimoNumero and not saoIguais):
        paraLoop += 1
    else:
        saoIguais = True

if (saoIguais):
    print('\n Sim') #\n serve para pular uma linha
else:
    print("\nNão")
'''
