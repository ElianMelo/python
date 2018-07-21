print('\033[31m-' * 20)
print('{:^20}'.format('Escola'))
print('-' * 20, '\033[m')

n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))

m = (n1 + n2) / 2

if m < 5:
    print('A sua média deu {:.1f} REPROVADO!'.format(m))
elif 5 <= m <= 6.9:
    print('A sua média deu {:.1f} RECUPERAÇÃO!'.format(m))
elif m >= 7:
    print('A sua média deu {:.1f} APROVADO!'.format(m))
