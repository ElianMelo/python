soma = cont = 0
while True:
    n = int(input("Escreva um número (999 para parar): "))
    if n == 999:
        break
    soma += n
    cont += 1
print(f"A soma dos {cont} números é igual a {soma}")
