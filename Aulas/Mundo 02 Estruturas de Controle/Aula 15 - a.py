# Gambiarra

'''n = s = 0
while n != 999:
    n = int(input("Digite um número: "))
    s += n
s -= 999
print("A soma vale {}".format(s))'''

# Forma Correta

n = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
# print("A soma vale {}".format(s))
print(f"A soma vale {s}")
