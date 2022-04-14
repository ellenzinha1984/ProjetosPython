# Exercício ano nascimento
nasc = int(input('Digite seu ano de nascimento: '))
ano = int(input('Digite o ano atual: '))
r = input('Você já fez aniversário este ano? S ou N')
idade = ano - nasc
if (idade >= 18 and r=='S'):
    print('Você tem {} anos'.format(idade))
    print('Você já pode tirar sua carteira de motorista!')