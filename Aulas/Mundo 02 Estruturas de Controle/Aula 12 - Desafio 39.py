from datetime import date

print('\033[36m-' * 20)
print('{:^20}'.format('Alistamento'))
print('-' * 20, '\033[m')

nasc = int(input('Você nasceu em qual ano? '))
ano = date.today().year

age = int(ano - nasc)

if age == 18:
    print('Hora de se alistar')
elif age < 18:
    print('Faltam {} ano(s) pra se alistar'.format(18 - age))
elif age > 18:
    print('O seu tempo de alistamento passou a {} ano(s)'.format(age - 18))
