frase = str(input("Escreva uma frase: "))
frase = frase.lower()
frase = frase.strip()
frase = frase.replace(" ", "")
i = False

num_letras = len(frase) - 1
comparacoes = int(num_letras / 2)

for c in range(0, comparacoes):
    if frase[c] != frase[num_letras - c]:
        i = True

print(" ")
if i == False:
    print("A sua frase é um palindromo")
else:
    print("A sua frase não é um palindromo")





