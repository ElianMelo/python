prm_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
num = 0
termos = -1
ini_termos = 9

while num != prm_termo + razao * ini_termos:
    num += razao
    print(num, end=" ")

while termos != 0:
    num = 0
    termos = int(input("\nVocê deseja ver mais quantos termos? "))
    if termos != 0:
        ini_termos += termos
        while num != prm_termo + razao * ini_termos:
            num += razao
            print(num, end=" ")
print("Fim do Programa")
