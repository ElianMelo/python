num = str(input('Digite um número entre 0 e 9999: '))

# Zero a esquerda
num = '{:>4}'.format(num)
num = num.replace(' ', '0')

# Separar e Classificar
num = list(num)

print('Unidade = {}'.format(num[3]))
print('Dezena  = {}'.format(num[2]))
print('Centena = {}'.format(num[1]))
print('Milhar  = {}'.format(num[0]))










