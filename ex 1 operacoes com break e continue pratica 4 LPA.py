# Exercicio operações matemáticas elaborado com break e continue

while True:
    n1 = float(input('Digite um valor: '))
    n2 = float(input('Digite outro valor: '))
    operacao = input(
        'Digite a operação desejada:\n 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n Qual a opção escolhida? ')
    print('Pressione a tecla s para sair.')
    # Usei o while pois não sei quantas operações serão executadas
    # O while True cria um loop infinito para o s
    # Eu coloquei os inputs dentro do true
    if (operacao=='1'):
        print('A soma entre {} e {} é {}.'.format (n1, n2, n1 + n2))
        continue
    elif (operacao=='2'):
        print('A subtração de {} e {} é {}.'.format(n1, n2, n1 - n2))
        continue
    elif (operacao=='3'):
        print('A multiplicação de {} por {} é {}.'.format(n1, n2, n1 * n2))
        continue
    elif (operacao=='4'):
        print('A divisão de {} por {} é {}.'.format(n1, n2, n1 / n2))
        continue
    elif (operacao =='s') or (operacao =='S'):
        print('Encerrando o programa...')
        break
    else:
        print('Escolha uma opção válida.')


    # Necessito pedir novamente as informações para não ficar mostrando a operação e resultado infinitamente!!
    # Continue faz com que já volte para o while

