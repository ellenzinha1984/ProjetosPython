# Exercício km percorridos
print('Exercício km percorridos')
km = float(input('Digite os quilômetros percorridos: '))
dias = int(input('Quantidade de dias que o carro foi alugado: '))
diaria = dias * 60
kmrodado = km * 0.15
total = diaria + kmrodado
print('Valor das diárias: R$ {}'.format(diaria))
print('Valor dos quilômetros rodados: R$ {}'.format(kmrodado))
print('O total a pagar é: R$', total)
