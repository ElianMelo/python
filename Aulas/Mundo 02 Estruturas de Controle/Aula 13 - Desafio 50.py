s = 0
for c in range(1, 7):
    n = int(input("Digite um valor : "))
    if n % 2 == 0:
        s += n
    else:
        s += 0
print("A soma dos valores pares é igual a {}".format(s))

