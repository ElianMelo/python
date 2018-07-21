while True:
    cont = 1
    n = int(input("Digite um número para ver sua tabuada: "))
    if n < 0:
        break
    while cont <= 10:
        print(f"{n} x {cont} = {n*cont}")
        cont += 1
    print("-"*40)
print("Fim do Programa")
