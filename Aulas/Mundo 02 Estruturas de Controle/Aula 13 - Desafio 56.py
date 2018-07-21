media = 0
mais_velho = "a"
mulheres = 0
maior = -999

for c in range(0, 4):
    # captura os dados
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo (masc/fem): "))
    sexo = sexo.lower()

    # verifica se foi digitado corretamente
    if sexo != "masc" and sexo != "fem":
        print("sexo inválido!")
        break
    print("")

    # nome do homem mais velho
    if sexo == "masc":
        if idade > maior:
            maior = idade
            mais_velho = nome

    # mulheres com menos de 20 anos
    if sexo == "fem":
        if idade < 20:
            mulheres += 1

    # calcula a média
    media += idade

# termina o calculo da média
media = media / 4

# mostra os resultados
print("A média de idade do grupo é {:.2f}".format(media))
if mais_velho == "a":
    print("Não há homens no grupo")
else:
    print("O nome do homem mais velho é {}".format(mais_velho))
print("Há {} mulher(es) com menos de 20 anos".format(mulheres))
