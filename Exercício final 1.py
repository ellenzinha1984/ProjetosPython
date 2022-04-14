# Atividade 1 - Lógica de Programação e Algoritmo
print('** Bem-vindo ao Atacado da Ellen Canossa Gagliardi Murata **')  # Identificador nome. Meu RU é 3967495
print('Digite a seguir os valores do produto e quantidades para cálculo dos descontos.')
valor = float(input('Digite o valor unitário do produto: R$ '))  # Recebe o valor do produto
qtde = int(input('Digite a quantidade de produtos comprada: '))  # Recebe a quantidade de produtos
sub = valor * qtde  # Produto de valor e quantidade para posterior cálculo de desconto.
if qtde > 0 and qtde < 10:  # Verificação da quantidade de unidades compradas, aqui pega as compras de 1 a 9 unidades.
    print('Você comprou {} produtos. O total a pagar é R${:.2f} (sem descontos para esta quantidade).'.format(qtde, sub))
elif qtde >= 10 and qtde < 100:  # Seleciona compras de 10 a 99 unidades
    total = sub - (sub*0.05)  # Cálculo de desconto de 5% para compras acima de 9 e menores de 99 unidades
    print('Você comprou {} produtos. O valor sem desconto é R${:.2f}.'.format(qtde, sub))
    print('Você recebeu um desconto de 5%, e o total a pagar é R${:.2f}'.format(total))
elif qtde >= 100 and qtde < 1000:  # Seleciona compras de 100 a 999 unidades
    total = sub - (sub*0.1)  # Cálculo de desconto de 10% para compras a partir de 100 até 999 unidades
    print('Você comprou {} produtos. O valor sem desconto é R${:.2f}.'.format(qtde, sub))
    print('Você recebeu um desconto de 10%, e o total a pagar é R${:.2f}'.format(total))
else:
    total = sub - (sub*0.15)  # Cálculo de desconto de 15%. Este else seleciona todas as compras acima de 1000 unidades
    print('Você comprou {} produtos. O valor sem desconto é R${:.2f}.'.format(qtde, sub))
    print('Você recebeu um desconto de 15%, e o total a pagar é R${:.2f}'.format(total))
