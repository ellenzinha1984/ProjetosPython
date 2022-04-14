# Exercício mutiplicação

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
cont = 1
mult = 0
while (cont <= n1):
    mult = mult + n2
    cont += 1
print('Resultado: {} x {} = {}'.format(n1, n2, mult))

