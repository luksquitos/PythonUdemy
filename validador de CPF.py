cpf = '16899535009'
novo_cpf = cpf[:9]
multiplicador = 10
digito_1 = digito_2 = somatorio = 0

for index in range(19):
    if index > 8:
        index -= 9
    somatorio += int(novo_cpf[index]) * multiplicador
    multiplicador -= 1

    if multiplicador == 2:
        conta = 11 - (somatorio % 11)
        multiplicador = 11
        if conta > 9:
            digito_1 = 0
            novo_cpf += str(digito_1)
