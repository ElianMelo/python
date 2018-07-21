import random
alun1 = input('Nome do aluno 1: ')
alun2 = input('Nome do aluno 2: ')
alun3 = input('Nome do aluno 3: ')
alun4 = input('Nome do aluno 4: ')
aluns = [alun1, alun2, alun3, alun4]
random.shuffle(aluns)
print("Ordem dos alunos é igual a : {}".format(aluns))

