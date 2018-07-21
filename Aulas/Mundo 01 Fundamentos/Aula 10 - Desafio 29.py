vel = float(input('Velocidade de seu carro: '))

if vel > 80:
    mlt = float(7 * (vel - 80))
    print('Você será multado! você deve pagar R${:.2f}'.format(mlt))
else:
    print('Você não será multado!')
