# Exercício operações entre números

n1 = int(input('Digite o número inicial do intervalo: '))
n2 = int(input('Digite o número final do intervalo: '))
cont = n1
somapar = 0
somaimpar = 0
somaintpositivo = 0
par = 0
impar = 0
intpositivo = 0
if (n1 < n2):
    while (cont <= n2):
        if (cont > 0):
            intpositivo += 1
            somaintpositivo = somaintpositivo + cont
        if (cont % 2 == 0):
            par += 1
            somapar = somapar + cont
        else:
            impar += 1
            somaimpar = somaimpar + cont
        cont += 1
    mediaintpositivo = somaintpositivo / intpositivo
    mediapar = somapar / par
    mediaimpar = somaimpar / impar
    print('No intervalo há {} números inteiros positivos e a média dos valores é {:.2f}'.format(intpositivo,somaintpositivo))
    print('No intervalo há {} números pares e a média dos valores é {:.2f}'.format(par,somapar))
    print('No intervalo há {} números ímpares e a média dos valores é {:.2f}'.format(impar,somaimpar))

else:
    print('Você digitou um valor inicial maior ou igual ao final. Encerrando o programa...')

