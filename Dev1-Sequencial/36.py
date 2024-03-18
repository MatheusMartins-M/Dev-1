from math import sqrt

base = float(input("Digite a base do retangulo: "))
altura = float(input("Digite a altura do retangulo: "))

area = base * altura
perimetro = (base + altura) * 2
diagonal_quadrada = base ** 2 + altura ** 2
diagonal = sqrt(diagonal_quadrada)

print("Perímetro: {}".format(perimetro))
print("Área: {}".format(area))
print("Diagonal: {:.2f}".format(diagonal))
