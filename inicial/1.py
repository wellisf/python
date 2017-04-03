'''
Faça um programa que peça dois números inteiros e imprima a soma desses dois números

Exemplo
	python 1.py
	number une: 4+8
	number tow: -1
	The sum is: 11
'''

# Function definition is here
# @p1 , @p2 numbers for sum
def sum(p1, p2):
	return p1 + p2

# Now you can call changeme function
n1 = int (input('number une: '))
n2 = int (input('number tow: '))
print "The sum is:", sum(n1,n2)
