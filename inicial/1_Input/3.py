# -*- coding: utf-8 -*-"

'''
Desafio do vídeo "Entrada de Dados": Reescreva o programa conta
Segundos para imprimir também a quantidade de dias,
ou seja, faça um programa em Python que dada a quantidade de segundos,
o programa "quebra" esse valor em dias, horas, minutos e segundos.
A saída deve estar no formato: a dias, b horas, c minutos e d segundos.

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

Entrada de Dados:
Por favor, entre com o número de segundos que deseja converter: 178615

Saída de Dados:
2 dias, 1 horas, 36 minutos e 55 segundos.
'''


def dayToSecond(second):
    return second*86400

second = float(input('Por favor, entre com o número de segundos que deseja converter:'))

day = second//86400

if (day - second/86400) != 0 :

    hour = day - second/86400

    if hour < 0 :
        hour = -1 * hour

    hour = hour * 24
    hour = hour//1

    if (hour- (day - second/86400)*24) != 0 :

        if ((day - second/86400)*24) < 0 :
            minute = (hour + (day - second/86400)*24)
        else:
            minute = (hour - (day - second/86400)*24)

        if minute < 0 :
            minute = (-1 * minute) *60

        temp = minute
        minute = minute//1

        temp = minute - temp

        if temp < 0 :
            temp = -1 * temp

        if temp != 0 :
            temp = (temp * 60)//1

print(int(day),"dias,",int(hour),"horas,",int(minute),"minutos e",int(temp),"segundos.")


