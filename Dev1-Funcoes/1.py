from math import pi


def calcula_volume(raio):
    vol = (4 * pi * (raio ** 3)) / 3
    return vol


valor = int(input("Digite o valor do raio: "))
volume = calcula_volume(valor)

print("O valor do volume no raio de {} é {:.2f}".format(valor, volume))
