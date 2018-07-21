num1 = float(input("Digite o 1° Valor: "))
num2 = float(input("Digite o 2° Valor: "))
maior = 0
menor = 0
opcao = 0

while opcao != 5:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa''')

    opcao = int(input("Qual opção? "))

    # Realiza a soma dos valores
    if opcao == 1:
        soma = num1 + num2
        print(" ")
        print("A soma de {} + {} = {}".format(num1, num2, soma))
        print(" ")

    # Realiza a multiplicação dos valores
    if opcao == 2:
        mult = num1 * num2
        print(" ")
        print("A multiplicação de {} * {} = {}".format(num1, num2, mult))
        print(" ")

    # Realiza a captura de novos valores
    if opcao == 3:
        if num1 >= num2:
            maior = num1
            menor = num2
        else:
            maior = num2
            menor = num1
        print(" ")
        print("O maior valor é {} e o menor valor é {}".format(maior, menor))
        print(" ")

    # Realiza a captura de novos valores
    if opcao == 4:
        num1 = float(input("Digite o 1° Valor: "))
        num2 = float(input("Digite o 2° Valor: "))
print("Fim do Programa")
