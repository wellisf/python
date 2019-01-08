

def partida():
	n=int(input("Quantas peças? "))
	m=int(input("Limite de peças por jogada? "))
	print()
	if not int(n%(m+1)==0) or n<=m:
		print("Computador começa!")
		print()
		while n>0:
			n=n-computador_escolhe_jogada(n, m)
			if n<=0:
				print("Fim do jogo! O computador ganhou!")
				break
			print("Agora restam", n, "peças no tabuleiro.")
			print()
			n=n-usuario_escolhe_jogada(n, m)
			if n<=0:
				print("Fim do jogo! Você ganhou!")
				break
			print("Agora restam", n, "peças no tabuleiro.")
			print()
	else:
		print("Você começa!")
		print()
		while n>0:
			n=n-usuario_escolhe_jogada(n, m)
			if n<=0:
				print("Fim do jogo! Você ganhou!")
				break
			print("Agora restam", n, "peças no tabuleiro.")
			print()
			n=n-computador_escolhe_jogada(n, m)
			if n<=0:
				print("Fim do jogo! O computador ganhou!")
				break
			print("Agora restam", n, "peças no tabuleiro.")
			print()
	

def campeonato():
		x=1
		voce=0
		comp=0
		while x<=3:
			print()
			print("**** Rodada", x, "****")
			print()
			n=int(input("Quantas peças? "))
			m=int(input("Limite de peças por jogada? "))
			print()
			if not int(n%(m+1)==0) or n<=m:
				print("Computador começa!")
				print()
				while n>0:
					n=n-computador_escolhe_jogada(n, m)
					if n<=0:
						print("Fim do jogo! O computador ganhou!")
						comp=comp+1
						break
					print("Agora restam", n, "peças no tabuleiro.")
					print()
					n=n-usuario_escolhe_jogada(n, m)
					if n<=0:
						print("Fim do jogo! Você ganhou!")
						voce=voce+1
						break
					print("Agora restam", n, "peças no tabuleiro.")
					print()
			else:
				print("Você começa!")
				print()
				while n>0:
					n=n-usuario_escolhe_jogada(n, m)
					if n<=0:
						print("Fim do jogo! Você ganhou!")
						voce=voce + 1
						break
					print("Agora restam", n, "peças no tabuleiro.")
					print()
					n=n-computador_escolhe_jogada(n, m)
					if n<=0:
						print("Fim do jogo! O computador ganhou!")
						comp=comp+1
						break
					print("Agora restam", n, "peças no tabuleiro.")
					print()
			x=x+1
		print()
		print("**** Final do campeonato! ****")
		print()
		print("Placar: Você", voce, "X", comp, "Computador")


def computador_escolhe_jogada(n, m):
	ini=m
	if n-m<0:
		while n-m!=0:
			m=m-1
	aux=m
	valor=m
	while valor>0:
		if (n-valor)%(m+1)==0:
			print("O computador tirou", valor, "peças")
			return valor
		valor=valor-1

	print("O computador tirou", aux, "peças")
	return aux

def usuario_escolhe_jogada(n, m):
	pecas = int(input("Quantas peças você vai tirar? "))
	while pecas>m or pecas<=0 or not pecas<=n:
		print()
		print("Oops! Jogada inválida! Tente de novo.")
		print()
		pecas = int(input("Quantas peças você vai tirar? "))
	print("Você tirou", pecas, "peça.")
	return pecas

print("Bem-vindo ao jogo do NIM! Escolha:")
print()
print("1 - para jogar uma partida isolada")
escolha = int(input("2 - para jogar um campeonato "))
print()

if escolha == 1:
	print("Voce escolheu uma partida isolada!")
	print()
	partida()
else:
	print("Voce escolheu um campeonato!")
	campeonato()
