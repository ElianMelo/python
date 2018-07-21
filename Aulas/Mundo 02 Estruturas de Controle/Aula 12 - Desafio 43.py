print('\033[36m-' * 20)
print('{:^20}'.format('Cálculo de IMC'))
print('-' * 20, '\033[m')

peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))

IMC = round(peso / (altura ** 2), 2)
frase = 'De acordo com o IMC {:.1f} você está'.format(IMC)

if IMC < 18.5:
    print('{} Abaixo do Peso'.format(frase))
elif 18.5 <= IMC < 25:
    print('{} no Peso Ideal'.format(frase))
elif 25 <= IMC < 30:
    print('{} com Sobrepeso'.format(frase))
elif 30 <= IMC <= 40:
    print('{} com Obesidade'.format(frase))
elif IMC > 40:
    print('{} com Obesidade Mórbida'.format(frase))
