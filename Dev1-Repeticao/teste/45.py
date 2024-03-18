valor = int(input())

maior = valor

for x in range(1, 3):
    valor = int(input())

    if valor > maior:
        maior, valor = valor, maior

print(maior)
