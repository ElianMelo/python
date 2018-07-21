from datetime import date

ano = date.today().year
s_mai = 0

for c in range(0, 7):
    nasc = int(input("Nasceu em qual ano? "))
    idade = ano - nasc
    if idade >= 21:
        s_mai += 1
print("{} pessoas são maiores de idade".format(s_mai))
print("{} pessoas não são maiores de idade".format(7 - s_mai))


