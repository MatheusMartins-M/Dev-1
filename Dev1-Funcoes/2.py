def calcula_media(nota1, nota2, nota3, qual_media):
    if qual_media == "a":
        media = (nota1 + nota2 + nota3) / 3
        return media

    elif qual_media == "p":
        peso1 = 5
        peso2 = 3
        peso3 = 2
        soma_notas = peso1*nota1 + peso2*nota2 + peso3*nota3
        soma_pesos = peso1 + peso2 + peso3
        media = soma_notas/soma_pesos
        return media

    elif qual_media == "h":
        media = 3 / (1/nota1 + 1/nota2 + 1/nota3)
        return media


nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))
nota_tres = float(input("Digite a terceira nota: "))
escolha = " "

while escolha != "z":
    print("a) Média aritmética")
    print("p) Média ponderada")
    print("h) Média harmônica")
    print("z) Sair do programa")
    escolha = str(input("Digite sua escolha: "))

    if escolha == "z":
        print("Programa encerrado")
    else:
        calculo = calcula_media(nota_um, nota_dois, nota_tres, escolha)
        print("A média das notas é igual a {:.2f}".format(calculo))
