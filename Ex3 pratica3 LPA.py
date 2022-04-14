# Exercício kwh consumido
print('** Cálculo de kWh consumidos **')
print('Escolha a opção de acordo com o tipo de instalação do local:')
print('R - Residencial')
print('C - Comercial')
print('I - Industrial')
inst = input('Digite a opção: ')
if (inst=='R' or inst=='r' or inst=='C' or inst=='c' or inst=='I' or inst=='i'):
    kwh = float(input('Digite o consumo de kWh do local: '))
    if (inst=='R' or inst=='r'):
        if (kwh <= 500):
            total = kwh * 0.4
            print('Residencial. Faixa de consumo até 500 kWh, total a pagar R${}'.format (total))
        else:
            total = kwh * 0.65
            print('Residencial. Faixa de consumo acima de 500 kWh, total a pagar R${}'.format (total))
    elif (inst=='C' or inst=='c'):
        if (kwh <= 1000):
            total = kwh * 0.55
            print('Comercial. Faixa de consumo até 1000 kWh, total a pagar R${}'.format(total))
        else:
            total = kwh * 0.6
            print('Comercial. Faixa de consumo acima de 1000 kWh, total a pagar R${}'.format (total))
    elif (inst=='I' or inst=='i'):
        if (kwh <= 5000):
            total = kwh * 0.55
            print('Industrial. Faixa de consumo até 5000 kWh, total a pagar R${}'.format(total))
        else:
            total = kwh * 0.6
            print('Industrial. Faixa de consumo acima de 5000 kWh, total a pagar R${}'.format(total))

else:
    print('Opção inválida!')