mais_18 = homens = mulher_20 = 0

while True:
    print("-"*50)
    print("{:^50}".format("Cadastre uma pessoa"))
    print("-"*50)
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    if idade >= 18:
        mais_18 += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulher_20 += 1
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar [S/N]: ")).strip().upper()[0]
    if continuar == "N":
        break
print("\nAnálise dos Dados")
print(f"\nHá {mais_18} pessoa(s) com mais de 18 anos")
print(f"Há {homens} homem(ns) no grupo")
print(f"Há {mulher_20} mulher(es) com menos de 20 anos")
