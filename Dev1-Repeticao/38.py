lista = []
soma = 0
media = 0
contador = 0
somaMaior = 0

for i in range(0, 8):
    valor = int(input('Digite um valor: '))
    lista.append(valor)

for i in range(0, len(lista)):
    soma += lista[i]

    if lista[i] > 20:
        somaMaior += lista[i]
        contador += 1

media = somaMaior / contador

print('A soma dos valores é {}'.format(soma))
print('A media dos valores maiores de 20 é {}'.format(media))