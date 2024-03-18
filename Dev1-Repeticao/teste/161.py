from math import factorial

escolha = 1
lista = []
fatorial = 0

while escolha >= 1:
    escolha = int(input("Digite um valor: "))

    if escolha >= 1:
        lista.append(escolha)

for i in range(0, len(lista)):
    fatorial = factorial(lista[i])
    lista[i] = fatorial

print(lista)