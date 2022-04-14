# Exercício porcentagem desconto
# Deve ser solicitado o preço de um produto e percentual de desconto
# Depois deve calcular e exibir valor de desconto e preço final
print('Exercício porcentagem de desconto')
preco = float(input('Digite o valor do produto: '))   #converter string para ponto flutuante
perc = float(input('Digite o percentual de desconto: '))
desconto = preco * (perc/100)
total = preco - desconto
pagar = 'O desconto é de R$ {} e o total a pagar com desconto é R$ {}' .format(desconto, total)
print(pagar)