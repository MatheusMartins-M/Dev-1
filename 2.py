def calculos(notaUm: float, notaDois: float, notaTres: float, operacao: str):
    if operacao == "A":
        media_A = (notaUm + notaDois + notaTres) / 3
        return media_A

    elif operacao == "P":
        pesoUm = 5
        pesoDois = 3
        pesoTres = 2
        soma_pesos = pesoUm + pesoDois + pesoTres

        media_P = ((notaUm * pesoUm) + (notaDois * pesoDois) + (notaTres * pesoTres)) / soma_pesos

        return media_P

    elif operacao == "H":
        a = 1 / notaUm
        b = 1 / notaDois
        c = 1 / notaTres

        media_H = 3 / (a + b + c)

        return media_H

testeUm = calculos(10, 9, 3, "A")
print(f"O resultado é: {testeUm: ,.2f}")

testeDois = calculos(10, 9, 3, "P")
print(f"O resultado é: {testeDois: ,.2f}")

testeTres = calculos(10, 9, 3, "H")
print(f"O resultado é: {testeTres: ,.2f}")