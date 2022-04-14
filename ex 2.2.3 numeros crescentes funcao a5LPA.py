# Exercícios números crescentes a5LPA
# Rotina deve receber 3 valores e colocá-los em ordem crescente

def cresc(v1 = 0, v2 = 0, v3 = 0):  # Aqui permito que os valores sejam opcionais
    if (v1 and v2 and v3):  # Aqui condiciono os if a fazer as verificações caso os valores não sejam nulos
        if ((v1 > v2) and (v1 > v3)):
            if (v2 > v3):
                print('Ordem crescente: {}, {} e {}'. format(v3,v2,v1),end='')
            else:
                print('Ordem crescente: {}, {} e {}'.format(v2, v3, v1), end='')
        elif ((v2 > v1) and (v2 > v3)):
            if (v1 > v3):
                print('Ordem crescente: {}, {} e {}'.format(v3, v1, v2), end='')
            else:
                print('Ordem crescente: {}, {} e {}'.format(v1, v3, v2), end='')
        elif ((v3 > v1) and (v3 > v2)):
            if (v1 > v2):
                print('Ordem crescente: {}, {} e {}'.format(v2, v1, v3), end='')
            else:
                print('Ordem crescente: {}, {} e {}'.format(v1, v2, v3), end='')

#Programa principal
print('** Números em ordem crescente **')
v1 = int(input('Digite o valor 1: '))
v2 = int(input('Digite o valor 2: '))
v3 = int(input('Digite o valor 3: '))
cresc(v1, v2, v3)