n = int(input("Digite um número: "))
for c in range(0, 10):
    print('{}.{} = {}'.format(n, c + 1, n * (c + 1)))
