def calcula_divores(numero1):
    divisores = 0
    for i in range(1, numero1 + 1):
        if numero1 % i == 0:
            divisores += 1
    
    return divisores


valor = int(input('Digite um número: '))
calculo = calcula_divores(valor)

print("O valor {} possui {} divisores".format(valor, calculo))
