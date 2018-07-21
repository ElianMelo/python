from random import choice

print('\033[34m-' * 20)
print('{:^20}'.format('Jokenpô'))
print('-' * 20, '\033[m')

j = input('Escolha entre Pedra, Papel ou Tesoura: ').strip().lower().replace(' ', '')
c = choice(['pedra', 'papel', 'tesoura'])

if j in 'pedra papel tesoura':
    if j == c:
        print('\033[35mEMPATE!\033[m o computador escolheu {}'.format(c.capitalize()))
    elif j == 'pedra' and c == 'tesoura':
        print('\033[32mVITÓRIA!\033[m o computador escolheu {}'.format(c.capitalize()))
    elif j == 'tesoura' and c == 'papel':
        print('\033[32mVITÓRIA!\033[m o computador escolheu {}'.format(c.capitalize()))
    elif j == 'papel' and c == 'pedra':
        print('\033[32mVITÓRIA!\033[m o computador escolheu {}'.format(c.capitalize()))
    elif c == 'pedra' and j == 'tesoura':
        print('\033[31mDERROTA!\033[m o computador escolheu {}'.format(c.capitalize()))
    elif c == 'tesoura' and j == 'papel':
        print('\033[31mDERROTA!\033[m o computador escolheu {}'.format(c.capitalize()))
    elif c == 'papel' and j == 'pedra':
        print('\033[31mDERROTA!\033[m o computador escolheu {}'.format(c.capitalize()))
else:
    print('Opção Inválida!')
