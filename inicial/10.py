'''
	Escreva um programa para calcular a reducao do tempo de vida de um fumante. Pergunte a
quantidade de cigarros fumados por dia e quantos anos ele ja fumou. Considere que um fumante
perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perdera. Exiba o
total de dias
'''
'''
   Fazendo uma regra de tres chegamos que 144 cigarros tiram 1 dia
   de vida da pessoa (1 dia = 1440 minutos = 144 cigarros)
'''

def yearsLost(perDays, years):	
	return (years*365*perDays)/144 

cigarettesPerDay =  int (input("Cigarettes per days: "))
yearsYouSmoked = float (input("Years you smoked: "))

print "Days of life lost ", yearsLost(cigarettesPerDay, yearsYouSmoked)