# Programa pares alternativo pares

inicial = int(input('Digite o valor  par inicial da contagem: '))
final = int(input('Digite o valor final da contagem: '))
x = inicial
for x in range(inicial,final,2):
    print(x)
    x += 1
