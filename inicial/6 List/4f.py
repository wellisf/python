'''

Removendo elementos repetidos

Escreva a função remove_repetidos que recebe como parâmetro 
uma lista com números inteiros, 
verifica se tal lista possui elementos repetidos e os remove. 
A função deve devolver uma lista correspondente à primeira lista, 
sem elementos repetidos. A lista devolvida deve estar ordenada.

Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?

#list.sort() um método

#sorted(list) uma função que retorna uma sort list

'''

number = [7,8,9,15,1,2,7,8,9,7]

def remove_repetidos(list):

	remove = []

	list.sort()

	for x in range(0,len(list)-1):

		if not (list[x] == list[x+1]):
			remove.append(list[x])

	remove.append(list[len(list)-1])

	return remove

#number.sort()

#print(number[:len(number)])

number = remove_repetidos(number)

print(number[:len(number)])