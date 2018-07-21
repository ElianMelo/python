a = float(input('Lado A de um triângulo: '))
b = float(input('Lado B de um triângulo: '))
c = float(input('Lado C de um triângulo: '))

print(' ')
if ((b - c) < a < b + c and
    (a - c) < b < a + c and
    (a - b) < c < a + b):
    print('Estes lados podem formar um triângulo')
else:
    print('Estes lados não podem formar um triângulo')
