prm_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
dez_termos = prm_termo

while dez_termos != prm_termo + (razao * 10):
    print(dez_termos, end=" ")
    dez_termos += razao
