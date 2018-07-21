n = int(input("Digite um número: "))
i = False

# Verifica se o número é 0 ou 1
if n == 0 or n == 1:
    i = True

# Verifica se é primo ou não
for c in range(2, n):
    if n % c == 0:
        i = True
        break

# Mostra o resultado
if i == False:
    print("O número {} é primo".format(n))
else:
    print("O número {} não é primo".format(n))









