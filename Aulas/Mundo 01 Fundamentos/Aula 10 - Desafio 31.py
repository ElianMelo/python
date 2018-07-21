km = float(input('Você percorreu quantos km? '))

if km <= 200:
    preço = (km * 0.5)
    print('você deve pagar R${:.2f} pela viagem'.format(preço))
else:
    preço = (km * 0.45)
    print('você deve pagar R${:.2f} pela viagem'.format(preço))











