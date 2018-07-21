maior = -999
menor = 999

for c in range(0, 5):
    p = float(input("Qual seu peso? (Kg) "))
    if p > maior:
        maior = p
    if p < menor:
        menor = p

print(" ")
print("O menor peso é {:.2f} Kg".format(menor))
print("O maior peso é {:.2f} Kg".format(maior))






