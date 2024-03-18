contador = 0

for i in range(1,13):
    valor = int(input("Digite um valor: "))
    if valor > 30 and valor < 60:
        contador += 1

print("Existe {} valor(es) entre 30 e 60".format(contador))