valor = int(input('Digite um valor: '))
contador = 0
media = 0
soma = 0

for i in range(1, valor+1):
    soma += i
    contador += 1

media = soma / contador

print('A média dos valores entre 1 e {} é igual a {}'.format(valor, media))
