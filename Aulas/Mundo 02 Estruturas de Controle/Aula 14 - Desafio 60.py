num = int(input("Digite um número: "))
fatorial = 1
aux = num

while aux != 1:
    if num != 0:
        fatorial *= aux
        aux -= 1
    else:
        fatorial = 1
        aux = 1
print("O fatorial de {} é {}".format(num, fatorial))
