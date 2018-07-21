from datetime import date

print('\033[34m-' * 40)
print('{:^40}'.format('Confederação Nacional de Natação'))
print('-' * 40, '\033[m')

age = int(input('Você nasceu em qual ano? '))
ano = date.today().year
idade = ano - age
frase = 'De acordo com nosso sistema sua categoria é'

if idade <= 9:
    print('{} MIRIM'.format(frase))
elif 9 < idade <= 14:
    print('{} INFANTIL'.format(frase))
elif 14 < idade <= 19:
    print('{} JUNIOR'.format(frase))
elif 19 < idade <= 25:
    print('{} SÊNIOR'.format(frase))
elif idade > 25:
    print('{} MASTER'.format(frase))
