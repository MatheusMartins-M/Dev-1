peso_inicial = float(input("Informe o peso (em kg): "))
peso_gramas = peso_inicial * 1000
novo_peso = peso_inicial + (peso_inicial * 0.12)
percent = int(input("Informe o percentual de engordamento: "))
novo_peso2 = peso_inicial + (peso_inicial * (percent / 100))

print("Peso em gramas -> {:.0f}".format(peso_gramas))
print("Peso com percentual de 12% -> {}".format(novo_peso))
print("Peso com percentual de {}% -> {}".format(percent, novo_peso2))
