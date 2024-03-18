quantidade_eleitores = int(input('Digite quantos eleitores: '))
votos_brancos = int(input('Digite quantos votos foram brancos: '))
votos_nulos = int(input('Digite quantos votos foram nulos: '))
votos_validos = int(input('Digite quantos votos foram válidos: '))

percentual_brancos = (votos_brancos / quantidade_eleitores) * 100
percentual_nulos = (votos_nulos / quantidade_eleitores) * 100
percentual_validos = (votos_validos / quantidade_eleitores) * 100

print("Brancos -> {:.0f}%".format(percentual_brancos))
print("Nulos -> {:.0f}%".format(percentual_nulos))
print("Validos -> {:.0f}%".format(percentual_validos))