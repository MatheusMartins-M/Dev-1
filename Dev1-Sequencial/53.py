salario_joao = 1200
conta1 = 200
conta2 = 120
juros = 0.02

conta1 = conta1 + (conta1*juros)
conta2 = conta2 + (conta2*juros)

salario_final = salario_joao - conta1 - conta2

print("O salário final de João é de R${}".format(salario_final))