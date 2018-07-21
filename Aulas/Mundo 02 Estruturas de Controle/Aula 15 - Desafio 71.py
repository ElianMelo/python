nota_50 = nota_20 = nota_10 = nota_1 = aux = 0
print("-"*50)
print("{:^50}".format("Bancão TOP"))
print("-"*50)
valor = int(input("Digite um valor a ser sacado: R$"))
while True:
    if valor >= 50:
        nota_50 = valor // 50
        aux = nota_50 * 50
        valor -= aux
    elif 50 > valor >= 20:
        nota_20 = valor // 20
        aux = nota_20 * 20
        valor -= aux
    elif 20 > valor >= 10:
        nota_10 = valor // 10
        aux = nota_10 * 10
        valor -= aux
    elif 10 > valor >= 1:
        nota_1 = valor // 1
        aux = nota_1 * 1
        valor -= aux
    else:
        break
print("\nAnálise dos Dados")
print(f"\n{nota_50} Notas de R$50,00")
print(f"{nota_20} Notas de R$20,00")
print(f"{nota_10} Notas de R$10,00")
print(f"{nota_1} Notas de R$1,00")

