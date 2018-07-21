print('\033[35m-' * 20)
print('{:^20}'.format('Triângulos'))
print('-' * 20, '\033[m')

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print(' ')

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Este lados podem formar um triângulo!')
    if r1 == r2 == r3:
        print('Sendo ele um triângulo Equilátero!')
    elif (r1 == r2 and r1 != r3 or
          r2 == r3 and r2 != r1 or
          r1 == r3 and r1 != r2):
        print('Sendo ele um triângulo Isósceles')
    elif r1 != r2 != r3:
        print('Sendo ele um triângulo Escaleno')
else:
    print('Este lados não podem formar um triângulo!')
