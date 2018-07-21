sexo = ""

while sexo != "M" and sexo != "F":
    sexo = input("Qual seu sexo?(M/F) ").upper()
    if sexo != "M" and sexo != "F":
        print("Sexo Inválido")
print("")
if sexo == "M":
    print("Você é do sexo Masculino")
else:
    print("Você é do sexo Feminino")
