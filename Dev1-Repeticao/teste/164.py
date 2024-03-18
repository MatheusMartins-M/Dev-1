escolha = int(input("Digite um valor inteiro: "))
divisores = 0

for x in range (1, escolha + 1):
    if escolha % x == 0:
        divisores += 1

if divisores == 2:
    print("O valor {} é um número primo".format(escolha))
else:
    print("O valor {} não é um número primo".format(escolha))
