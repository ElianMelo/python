total = mais_1000 = menor = cont = 0
nome_barato = " "
print("-"*50)
print("{:^50}".format("Loja"))
print("-"*50)
while True:
    nome = str(input("Nome do produto: ")).strip()
    preco = float(input("Preço do produto: R$"))
    continuar = " "
    while continuar not in "sn":
        continuar = str(input("Quer continuar? [s/n] ")).strip().lower()[0]
    total += preco
    if preco > 1000:
        mais_1000 += 1
    cont += 1
    if cont == 1:
        menor = preco
        nome_barato = nome
    if preco < menor:
        menor = preco
        nome_barato = nome
    print(" ")
    if continuar == "n":
        break
print("Análise de Dados")
print(f"O total gasto na compra foi de R${total:.2f}")
print(f"{mais_1000} produto(s) custa(m) mais de R$1000")
print(f"O nome do produto mais barato é {nome_barato} custando R${menor:.2f}")
