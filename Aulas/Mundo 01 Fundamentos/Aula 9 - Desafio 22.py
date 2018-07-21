nome = str(input('Escreva seu nome: '))
nome = nome.strip()

# Exclui espaço
nome_esp = nome.split()
nome_esp = ' '.join(nome_esp)

# Vai fazer a contagem de letras
nome_div = nome.split()

fn_01 = ' '.join(nome_div)
fn_02 = len(fn_01) - (len(nome_div) - 1)

# Quantidade de letras do primeiro nome
nome_pri = nome.split()

print('Nome maiúsculo: {}'.format(nome_esp.upper()))
print('Nome minúsculo: {}'.format(nome_esp.lower()))
print('A quantidade de letras ao todo é {}'.format(fn_02))
print('O primeiro nome tem {} letras'.format(len(nome_pri[0])))
