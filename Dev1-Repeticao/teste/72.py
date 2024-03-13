lista = []
produto = 1

for x in range(1, 11):
    valor = int(input())

    if valor % 2 == 0:
        lista.append(valor)

for i in range(0, len(lista)):
    produto *= lista[i]


print(lista)
print(produto)

