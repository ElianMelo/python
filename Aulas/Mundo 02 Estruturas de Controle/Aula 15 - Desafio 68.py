from random import randint
v = "Par ou Impar"
print("-"*40)
print("{:^40}".format("Par ou Impar"))
print("-"*40)
vitorias = 0

while True:
    computador = randint(0, 10)
    jogador = int(input("Digite um número: "))
    par_impar = " "
    while par_impar not in "PI":
        par_impar = str(input("Par/Impar (P/I): ")).strip().upper()[0]
    soma = computador + jogador
    print(" ")
    print(f"Você jogou {jogador} e o computador {computador} a soma foi {soma}")
    if soma % 2 == 0 and par_impar == "P":
        vitorias += 1
        print("Jogador venceu")
    elif soma % 2 != 0 and par_impar == "P":
        print("Computador venceu")
        break
    elif soma % 2 == 0 and par_impar == "I":
        print("Computador venceu")
        break
    elif soma % 2 != 0 and par_impar == "I":
        vitorias += 1
        print("Jogador venceu")
    print(" ")
print(f"\nFim do Jogo você ganhou {vitorias} partida(s)")
