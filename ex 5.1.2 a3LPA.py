# Exercício formas de pagamento e descontos
print('Formas de pagamento')
compra = float(input('Digite o valor total da compra: '))
print('Escolha a forma de pagamento:')
print('1 - À vista')
print('2 - Parcelado em 3x')
print('3 - Parcelado em 5x')
print('4 - Parcelado em 10x')
parc = int(input('Digite a opção: '))
if (parc==1):
    desc = compra * 0.05
    total = compra - desc
    print('Pagamento à vista, seu desconto é de R${}, total a pagar: R${}.'.format(desc, total))
elif (parc==2):
    div = compra / 3
    total = compra
    print('Pagamento em 3x, parcelas de R${} sem acréscimo, total a pagar R${}'.format(div, total))
elif (parc==3):
    acr = compra * 0.02
    total = compra + acr
    div = total / 5
    print('Pagamento em 5x, parcelas de R${} com acréscimo de 2%, total a pagar R${}'.format(div, total))
elif (parc==4):
    acr = compra * 0.08
    total = compra + acr
    div = total / 10
    print('Pagamento em 10x, parcelas de R${} com acréscimo de 8%, total a pagar R${}'.format(div, total))
else:
    print('Opção de pagamento inválida!')