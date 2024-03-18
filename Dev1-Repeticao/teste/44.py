i = 0
contadorD = 0
contadorF = 0


while i < 10:
    valores = int(input("Digite um valor: "))

    if valores >= 10 and valores <= 30:
        contadorD += 1

    else:
        contadorF += 1

    i += 1

print("{0} estão no intervalo".format(contadorD))
print("{0} não estão no intervalo".format(contadorF))