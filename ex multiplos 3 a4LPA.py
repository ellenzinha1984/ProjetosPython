# Múltiplos de 3

inicial = int(input('Digite o valor  par inicial da contagem: '))
final = int(input('Digite o valor final da contagem: '))
x = inicial
while(x <= final):
    if (x % 3 == 0):
        print(x)
    x += 1
