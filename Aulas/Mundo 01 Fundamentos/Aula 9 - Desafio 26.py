frase = str(input('Digite uma frase: '))

# formatação
frase = frase.lower()
frase = frase.strip()

# Procura e Contagem
frase1 = frase.find('a')
frase2 = frase.rfind('a')
frase = frase.count('a')

print('A letra a, aparece {} vez(es)'.format(frase))
print('Sua primeira aparição ocorre na posição {}'.format(frase1+1))
print('Sua última aparição ocorre na posição {}'.format(frase2+1))






