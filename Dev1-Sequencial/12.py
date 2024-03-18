altura = float(input('Informe a altura da pessoa (em metros): '))
sexo = str(input('Informe o sexo: '))

if sexo == "homem":
    peso_ideal = 72.7 * altura - 58
elif sexo == "mulher":
    peso_ideal = 62.1 * altura - 44.7

peso = float(input("Informe o peso da pessoa (em kg): "))

if peso > peso_ideal:
    print("Acima do peso")
else:
    print("Abaixo do peso")
