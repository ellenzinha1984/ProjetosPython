#Exercício que lê nome, altura e peso e calcula IMC
#Programa vai cadastrar um número indefinido de dados em uma lista e no final imprimir a lista completa

def lista(lista):
    itens = 0
    media = 0
    for i in range(0, len(lista), 1):
        itens += 1  #Contagem de cadastros da lista
    print('A lista tem {} cadastros.'.format(itens))


def valida_dado(op):
    while (op < 1 or op > 2):  #Função que exige que usuário escolha apenas 1 ou 2
        print('Opção inválida! Digite uma opção válida:\n1 - Novo Cadastro\n2 - Sair\n')
        op = int(input('Opção desejada: '))
        continue

imc = lambda altura, peso: peso / (altura * altura)  #Função para o IMC

dados = []
print('* Cálculo de IMC *')

while True:
    nome = input('Digite o nome: ')
    altura = float(input('Digite a altura em metros: '))
    peso = float(input('Digite o peso em kg: '))
    x = imc(peso, altura)  #Aqui chamo a função lambda para o IMC usando peso e altura
    dados.append([nome, altura, peso, x])
    print('\n')
    resp = int(input('Digite 1 para continuar ou 2 para sair:  '))
    valida_dado(resp)
    if resp == 2:
        print('Encerrando o programa...')
        break
lista(dados)
print('Cadastros: ', dados)
menor = 99
for i in range(0, len(dados), 1):  #Farei a varredura dos constantes na lista de um em um
    if (dados[i][3] <  menor):
        menor = dados[i][3]
print('O menor IMC é {:.2f}'.format(menor))
maior = 0
for j in range(0, len(dados), 1):  #Farei a varredura dos constantes na lista de um em um
    if(dados[j][3] > maior):
        maior = dados[j][3]
print('O maior IMC é {:.2f}'.format(maior))





