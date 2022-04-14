# Exercício números primos 2 a 99

for numero in range (2, 100, 1):
    flag = 0  # variável vai alterar seu valor se o número não for primo
    for i in range(2, numero, 1):
        if (numero % i == 0):  # aqui testa que se o número for divisível por qqer valor não é primo
            flag = 1
            break
    if (not flag):
        print(numero)