# Exercício soma números
print('Exercício soma de números')
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
soma = num1 + num2
print('A soma de {} e {} é: {}'.format(num1, num2, soma))
print('\n')


# Exercício dia hora segundos
print('Exercício segundos')
dia = int(input ('Digite o número de dias '))
hora = int(input('Digite o número de horas '))
min = int(input('Digite o número de minutos '))
seg = int(input('Digite o número de segundos '))
# 1 dia = 24h, 1 hora = 60 min, 1 min = 60 seg
# dias em horas
valor = (dia * 24 * 60 * 60) + (hora * 60 * 60) + (min * 60) + seg
total = 'Modo clássico: O total de segundos do período digitado é: %i' % valor
print(total)
print('\n')
total = 'Modo moderno: O total de segundos do período digitado é: {}' .format(valor)
print(total)
print('\n')

# Exercício porcentagem desconto
print('Exercício porcentagem de desconto')
# Programa deve pedir o valor do produto, valor da porcentagem de desconto e mostrar o desconto aplicado
preco = float(input('Digite o valor do produto: '))
perc = float(input('Digite o percentual de desconto: '))
desconto = preco * (perc/100)
total = preco - desconto
pagar = 'O desconto é de R$ {} e o total a pagar com desconto é R$ {}' .format(desconto, total)
print(pagar)

# Exercício converter temperatura
print('Convertendo Celsius para Farenheit')
tempc = float(input('Digite a temperatura em Celsius a ser convertida: '))
far = ((9 * tempc) / 5) + 32
temperatura = 'A temperatura em Farenheit é: {}'.format(far)
print(temperatura)
