termos = int(input("Você deseja quantos termos? "))
fibo1 = 0
fibo2 = 1

if termos == 1:
    print("0", end=" ")
elif termos == 2:
    print("0 1", end=" ")
else:
    print("0 1", end=" ")
    termos -= 2
    while termos != 0:
        termos -= 1
        fibo = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = fibo
        print(fibo, end=" ")