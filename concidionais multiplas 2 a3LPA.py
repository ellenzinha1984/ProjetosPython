# Algoritmo para nome e idade e comparar
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
if (nome == 'Ellen'):
    print('Seu nome é {} e você tem {} anos.'.format(nome,idade))
elif (idade < 18):
    print('Você é menor de idade.')
elif (idade > 100):
    print('Você possivelmente não existe!!')
else:
    print ('Você não é Ellen. Seu nome é {} e sua idade é {}'.format(nome, idade))