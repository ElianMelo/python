from random import randint

n1 = randint(0, 5)
n2 = int(input('Digite um número entre 0 e 5: '))

if n1 == n2:
    print('Você Venceu!')
else:
    print('Você Perdeu! o número era {}'.format(n1))

