dias = int(input('Foi alugado por quantos dias? '))
km = float(input('Quantidade de km rodados? '))
r = (60 * dias) + (km * 0.15)
print('O preço a se pagar é de R${:.2f}'.format(r))

