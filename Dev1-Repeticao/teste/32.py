valor = int(input("Digite um valor a ser calculado: "))
contador = 1

while contador <= 10:
    resultado = valor * contador
    print("{0} x {1} = {2}".format(contador, valor, resultado))
    contador += 1

print()