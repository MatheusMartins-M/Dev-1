import math


def calcula_volume(raio):
    volume = (4 * math.pi * (raio ** 3)) / 3

    return volume

raio = calcula_volume(5)

print(f"O resultado é: {raio:,.2f}")