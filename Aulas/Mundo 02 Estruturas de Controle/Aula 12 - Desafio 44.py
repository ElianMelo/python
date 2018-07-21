print('\033[34m-' * 30)
print('{:^30}'.format('Formas de pagamento'))
print('-' * 30, '\033[m')

prod = float(input('Qual o valor do produto? R$'))
print(' ')

print('Opção 1: À vista dinheiro/cheque')
print('Opção 2: À vista no cartão')
print('Opção 3: Em até 2x no cartão')
print('Opção 4: 3x ou mais no cartão')
print(' ')
opc = int(input('Qual opção você deseja? '))

print(' ')
if opc == 1:
    prod = prod - (prod * 0.10)
    print('O preço do produto será R${}'.format(prod))
elif opc == 2:
    prod = prod - (prod * 0.05)
    print('O preço do produto será R${}'.format(prod))
elif opc == 3:
    print('O preço do produto será R${}'.format(prod))
elif opc == 4:
    prod = prod + (prod * 0.20)
    print('O preço do produto será R${}'.format(prod))
else:
    print('Opção Inválida')
