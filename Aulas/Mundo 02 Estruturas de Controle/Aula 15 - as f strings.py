nome = "José"
idade = 33
print(f"O {nome} tem {idade} anos.") # PYTHON 3.6+
print("O {} tem {} anos.".format(nome, idade)) # PYTHON 3
print("O %s tem %d anos." % (nome, idade)) # PYTHON 2

nome = "José"
idade = 33
salário = 987.3
print(f"O {nome:~^20} tem {idade} anos e ganha R${salário:.2f}")
