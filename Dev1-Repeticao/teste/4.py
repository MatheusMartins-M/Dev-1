contador = 0
soma = 0

for x in range (1, 51):
    if x % 2 == 0:
        contador += 1
        soma += x

print(f"Foram utilizados {contador} números para chegar ao resultado {soma}")