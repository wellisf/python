#Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.

# amount() receive @number ^@elevated, return isqual amount of potency
def amount(number, elevated):
	#str() cast, len() amout of char
	return (len(str(number**elevated)))


print  amount(2, 10)