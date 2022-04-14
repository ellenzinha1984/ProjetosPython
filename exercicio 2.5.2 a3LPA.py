# Exercício bônus funcionário
salario = float(input('Digite seu salário: '))
tempo = int(input('Digite seu tempo de empresa: '))
if (tempo >5):
    bon = salario * 0.2
    print('Você tem {} anos de empresa, portanto receberá bonificação de 20% (R${})'.format(tempo, bon))
else:
    bon = salario * 0.1
    print('Você tem {} ano(s) de empresa, portanto receberá bonificação de 10% (R${})'.format(tempo, bon))