i = "S"
cont = 0
soma = 0
maior = 0
menor = 0

while i == "S":
    num = int(input("Digite um valor: "))
    i = input("Deseja continuar? (S/N)").upper()
    cont += 1
    soma += num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print("A média dos {} valores é {}".format(cont, media))
print("O menor valor foi {} é o maior valor foi {}".format(menor, maior))
