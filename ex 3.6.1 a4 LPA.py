# Exercício números positivos

numeros = 0
soma = 0
num = 0
while True:
    num = int(input('Digite um número inteiro: '))
    if num < 0:
        continue
    if not num:
        break
    soma += num
    numeros += 1
media = soma / numeros
print ('A média de valores é: {:.2f}.'.format(media))
