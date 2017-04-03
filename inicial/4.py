'''

Faça um programa que calcule o aumento de um salário. 
Ele deve solicitar o valor do salário 
e a porcentagem do aumento. 

Exiba o valor do aumento e do novo salário.

'''

def  newSalary(oldSalary, increase):
	
	return (oldSalary + (increase/100)*oldSalary)


salary = float(input("Type your salary "))
increase = float(input("Type the percentage of the increase "))

print(newSalary(salary,increase))