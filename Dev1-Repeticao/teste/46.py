valor = int(input())

maior = valor
menor = valor

for x in range(1, 9):
    valor = int(input())

    if valor > maior:
        maior = valor

    else:
        menor = valor

print(maior, menor)