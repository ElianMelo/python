print('\033[34m-' * 20)
print('{:^20}'.format('Conversor'))
print('-' * 20, '\033[m')

print('Opção 1: Binário\n'
      'Opção 2: Octal\n'
      'Opção 3: Hexadecimal')

opcao = (int(input('Qual opção? ')))
num = int(input('Digite o valor a ser convertido: '))

if opcao == 1:
    print('O número {} convertido é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} convertido é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} convertido é {}'.format(num, hex(num)[2:]))
else:
    print('A opção {} não é valida'.format(opcao))
