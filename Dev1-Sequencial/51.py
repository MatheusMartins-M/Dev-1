salario_fixo = float(input("Informe o salário do funcionario: "))
vendas = float(input("Informe o valor das vendas: "))
comissao = 0.04

print("A comissão foi de R${:.2f}".format(vendas*comissao))

salario_final = salario_fixo + (vendas * comissao)

print("O salário final do funcionario é de R${:.2f}".format(salario_final))