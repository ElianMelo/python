from random import randint

comp = randint(0, 10)
jog = 0
cont = 0

while comp != jog:
    jog = int(input("Qual sua jogada? "))
    cont += 1

print(" ")
print("Parabens você ganhou!")
print("Você precisou de {} tentativa(s) o número escolhido foi {}".format(cont, comp))
