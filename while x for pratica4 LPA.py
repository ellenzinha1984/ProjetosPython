# Sequência com for e while

# Inteiros de 3 até 12 (12 incluso) com while
print('Inteiros de 3 a 12 com while:')
cont = 3
while (cont <=12):
    print(cont)
    cont +=1
print('\n')

# Inteiros de 3 até 12 (12 incluso) com for
print('Inteiros de 3 a 12 com for:')
for num in range(3,13,1):
    print(num)
print('\n')

# Inteiros de 0 até 9, excluindo 9, com passo de 2 com while
print('Inteiros de 0 a 9 excluindo 9 e passo de 2 com while:')
c = 0
while (c<9):
    print(c)
    c += 2
print('\n')

# Inteiros de 0 até 9, excluindo 9, com passo de 2 com for
print('Inteiros de 0 a 9 excluindo 9 e passo de 2 com for:')
for numero in range(0,9,2):
    print(numero)