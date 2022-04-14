# Algoritmo escolha frutas - maçã, banana ou laranja
fruta = int(input('Digite uma opção:\n 1 - maçã\n 2 - laranja\n 3 - banana\n Opção: '))
qtde = int(input('Digite quantas unidades da fruta desejada: '))
if (fruta == 1):
    total = qtde * 2.3
    print('O total a pagar pelas maçãs é R${}'.format(total))
else:
    if (fruta == 2):
        total = qtde * 3.6
        print('O total a pagar pelas laranjas é R${}'.format(total))
    else:
        if (fruta == 3):
         total = qtde * 1.85
         print('O total a pagar pelas bananas é R${}'.format(total))
        else:
         print('Produto inexistente!')