# Exercício frase

frase = input('Digite uma frase de 10 a 30 caracteres: ')
tam = len(frase)
while (tam < 10) or (tam > 30):
    print('Tamanho de frase incorreto!')
    frase = input('Digite uma frase de 10 a 30 caracteres: ')
    tam = len(frase)
    # Esse while vai condicionar a frase digitada a ter 10 a 30 caracteres
print('Com espaços: {}'.format(frase))
print('Sem espaços: ', end='')  # Aqui forço o print a colocar tudo sem espaços
for i in range(0, tam, 1):
    if (frase[i] != ' '):  # Aqui se o caractere da frase for diferente de nulo ele imprime
        print(frase[i], end='')