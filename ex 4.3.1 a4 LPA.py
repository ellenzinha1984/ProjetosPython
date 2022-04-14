# Exercício média 1 a 100

soma = 0
cont = 0
for i in range(1,101):
    if (i % 2 ==0):
        soma += i
        cont += 1
media = soma / cont
print('A média dos números pares de 1 a 100 é {}'.format(media))
