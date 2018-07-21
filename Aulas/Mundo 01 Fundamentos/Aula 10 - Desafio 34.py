salario = float(input('Digite seu salário: R$'))
if salario > 1250:
    nv_slr = salario + (salario * 0.10)
else:
    nv_slr = salario + (salario * 0.15)
print('Seu novo salário é R${:.2f}'.format(nv_slr))



