ganho_hora = float(input("Digite o valor ganho por hora: "))
horas = int(input("Digite a quantidade de horas trabalhadas: "))

salario = ganho_hora * horas

print("O salario é de R${:.2f}".format(salario))