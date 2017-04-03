'''
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
usuario, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preco a pagar,
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
'''

def pay(km, days):
	return (days*60 + km*0.15)

km = float (input(" The value of Km: "))
days = int (input(" Amount of days: "))

print "The value pay is: ", pay(km,days) 
