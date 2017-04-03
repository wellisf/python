'''

Escreva um programa que leia a quantidade de dias, 
horas, minutos e segundos do usuário. 

Calcule o total em segundos.

'''

def secund(hours, minute, secunds):
	


	return (secunds + minute*60 + hours*3600)
 


h = int(input('Type the Hours '))
m = int(input('Type the Minute '))
s = int(input('Type the Secunds '))

print (secund(h,m,s))

