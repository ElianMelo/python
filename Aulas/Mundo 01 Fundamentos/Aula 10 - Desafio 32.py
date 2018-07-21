ano = int(input('Digite um ano: '))

r1 = ano % 4
r2 = ano % 100
r3 = ano % 400

if (r1 == 0 and r2 != 0 and r3 != 0 or
    r1 == 0 and r2 == 0 and r3 == 0):
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
