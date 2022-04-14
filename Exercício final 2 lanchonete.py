#Atividade 2 - Lógica de Programação e Algoritmo
print('Bem-vindo(a) à Lanchonete da Ellen Canossa Gagliardi Murata') #Identificador pessoal - meu RU é 3967495
print('-' * 56)
print('+', '-' * 20, ' CARDÁPIO ', '-' * 20, '+')
print('| Cod. |              DESCRIÇÃO              |VALOR  R$|')
print('+', '-' * 52, '+')
print('| 100  |           Cachorro-Quente           |   9,00  |')
print('| 101  |        Cachorro-Quente Duplo        |  11,00  |')
print('| 102  |                X-Egg                |  12,00  |')
print('| 103  |              X-Salada               |  13,00  |')
print('| 104  |              X-Bacon                |  14,00  |')
print('| 105  |               X-Tudo                |  17,00  |')
print('| 200  |          Refrigerante Lata          |   5,00  |')
print('| 201  |             Chá Gelado              |   4,00  |')
print('+', '-' * 52, '+')
total = 0  #Variável para a soma do total a ser pago
valor = 0  #Variável para os valores individuais dos produtos
while True:  #O while é usado pois não sabemos quantas operações serão executadas, e while true cria loop infinito
    cod = int(input('Escolha o código da opção desejada: '))  #Aqui o input para receber o código do produto
    if cod == 100:  #Aqui iniciam as verificações do código digitado com if e elif
        valor = 9.00
        print('Você escolheu Cachorro-quente no valor de R${:.2f} '.format(valor))
        total += valor  #Acumulador dos valores de cada produto
        valor = 0
    elif cod == 101:
        valor = 11.00
        print('Você escolheu Cachorro-quente Duplo no valor de R${:.2f} '.format(valor))
        total += valor
        valor = 0
    elif cod == 102:
        valor = 12.00
        print('Você escolheu X-Egg no valor de R${:.2f} '.format(valor))
        total += valor
        valor = 0
    elif cod == 103:
        valor = 13.00
        print('Você escolheu X-Salada no valor de R${:.2f} '.format(valor))
        total += valor
        valor = 0
    elif cod == 104:
        valor = 14.00
        print('Você escolheu X-Bacon no valor de R${:.2f} '.format(valor))
        total += valor
        valor = 0
    elif cod == 105:
        valor = 17.00
        print('Você escolheu X-Tudo no valor de R${:.2f} '.format(valor))
        total += valor
        valor = 0
    elif cod == 200:
        valor = 5.00
        print('Você escolheu Refrigerante lata no valor de R${:.2f} '.format(valor))
        total += valor
        valor = 0
    elif cod == 201:
        valor = 4.00
        print('Você escolheu Chá Gelado no valor de R${:.2f} '.format(valor))
        total += valor
        valor = 0
    else:  #Aqui o else para validar o código desejado (tem que ser um dos descritos)
        print('Escolha uma opção válida!')
        continue  #O continue faz com que o programa volte para o while até que uma opção válida seja digitada
    print('O subtotal dos produtos está em: R${:.2f}'.format(total))
    print('Deseja pedir mais algum item?')
    print('1 - SIM')
    print('2 - NÃO')
    opcao = int(input('Escolha: '))  #Aqui a opção para o usuário continuar ou não escolhendo produtos
    if opcao == 1:  #Opção SIM (continuar)
        continue
    elif opcao == 2:  #Opção NÃO (encerrar)
        print('O total a ser pago é: R${:.2f}'.format(total))  #Aqui eu mostro o total dos produtos acumulados a pagar
        print('Obrigado pela preferência! :)')
        break  #O break quebra o laço do while no caso de o usuário digitar opção para não pedir mais nada



