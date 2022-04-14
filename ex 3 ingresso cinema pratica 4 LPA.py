# Exercício valores ingresso cinema pratica 4 LPA
# valores do ingresso de acordo com a idade da pessoa

total = 0
dinheiro = 0
while True:
    print('Digite a opção. Para encerrar, digite "sair".')
    idade = input('Digite a idade: ')
    if idade == 'sair':
        break
    idade = int(idade)  # Aqui converti a string em inteiro
    if idade < 3:
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30
        else:
            ingresso = 15
    dinheiro = dinheiro + ingresso  # Pode ser dinheiro += ingresso
    total += 1
media = dinheiro / total
print('Total de pessoas: {}'.format(total))
print('Total arrecadado: {}'.format(dinheiro))
print('Média de valor: {:.2f}'.format(media))
