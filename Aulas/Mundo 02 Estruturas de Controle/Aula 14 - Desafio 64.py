num = 0
total = 0
cont = 0

while num != 999:
    num = int(input("Digite um número: "))
    if num != 999:
        cont += 1
        total += num
print("A soma dos {} números é igual a {}".format(cont, total))
