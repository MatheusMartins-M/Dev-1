def ve_conceito(media):
    if media <= 4.9:
        conceito = "D"
        return conceito

    elif 5 <= media <= 6.9:
        conceito = "C"
        return conceito

    elif 7 <= media <= 8.9:
        conceito = "B"
        return conceito

    elif 9 <= media <= 10:
        conceito = "A"
        return conceito


valor = float(input("Digite a media do aluno: "))
conceito_aluno = ve_conceito(valor)

print("O conceito do aluno foi: {}".format(conceito_aluno))
