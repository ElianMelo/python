print('\033[34m-' * 20)
print('{:^20}'.format('Comparador'))
print('-' * 20, '\033[m')

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

if n1 > n2:
    print('O Primeiro Valor é maior')
elif n2 > n1:
    print('O Segundo Valor é maior')
elif n1 == n2:
    print('Os dois valores são iguais')
