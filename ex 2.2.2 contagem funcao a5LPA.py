# Exercício contagem com funções

def contagem(f, i = 0, p = 1):
    for i in range(i, f, p):
        print('{} '.format(i), end='')
    print('\n')

# Programa principal
contagem(10,1,1)
contagem(10,0,2)
contagem(20)

