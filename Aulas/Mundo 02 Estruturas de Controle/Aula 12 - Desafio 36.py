print('\033[34m-' * 20)
print('{:^20}'.format('Empréstimo'))
print('-' * 20)
print('\033[m')

vlr_csa = float(input('Qual é o valor da casa? R$'))
slr = float(input('Qual é seu salário? R$'))
ano = int(input('Você vai pagar em quantos anos? '))

meses = ano * 12
nv_slr = slr * 0.3
nv_vlr_csa = vlr_csa / meses

print(' ')
if nv_vlr_csa > nv_slr:
    print('Empréstimo \033[31mNEGADO!\033[m O valor mensal da casa é de \033[32mR${:.2f}\033[m \n'
          'superior a 30% de seu salário que é \033[32mR${:.2f}\033[m!'.format(nv_vlr_csa, nv_slr))
else:
    print('Empréstimo \033[34mACEITO!\033[m você deverá pagar \033[32mR${:.2f}\033[m por mês'.format(nv_vlr_csa))
