algo = input("Escreva Algo: ")

print(algo)
print('Tipo', type(algo))
print('Número ? ', algo.isdecimal())
print('Número ? ', algo.isnumeric())
print('Digito ? ', algo.isdigit())
print('Letra ? ', algo.isalpha())
print('Letra ou Número ? ', algo.isalnum())
print('Maiúsculo ? ', algo.isupper())
print('Minúsculo ? ', algo.islower())
print('Identificador ? ', algo.isidentifier())
print('Pode ser escrito ? ', algo.isprintable())
print('É um espaço ? ', algo.isspace())
print('É um título ? ', algo.istitle())
