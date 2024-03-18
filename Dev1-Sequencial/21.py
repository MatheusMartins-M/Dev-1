valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite um valor: '))
valor3 = float(input('Digite um valor: '))

print("Primeiro valor: {:.0f}, segundo valor: {:.0f}, terceiro valor: {:.0f}".format(valor1, valor2, valor3))

produto = valor1 * valor2 * valor3
soma = valor1 + valor2 + valor3

print('A soma entre {:.0f}, {:.0f} e {:.0f} é {}'.format(valor1, valor2, valor3, soma))
print('O produto entre {:.0f}, {:.0f} e {:.0f} é {}'.format(valor1, valor2, valor3, produto))
