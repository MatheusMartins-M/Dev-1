salario = float(input('Digite o salário: '))
reajuste = int(input('Digite o percentual de reajuste: '))

salario_final = salario + (salario * (reajuste/100))

print("Salário reajustado: R${}".format(salario_final))
