from math import factorial


def calcula_fatorial(valor):
    fatorial = factorial(valor)
    return fatorial


numero = int(input('Digite um valor: '))
calculo = calcula_fatorial(numero)

print("O valor fatorial de {} é {}".format(numero, calculo))
