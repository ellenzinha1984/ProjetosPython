# Exercício idade e sexo

idade = int(input('Digite sua idade: '))

while idade > 0:
    sexo = input('Digite o sexo (M ou F): ')
    if sexo == 'M' or sexo == 'm':
        print('Boa noite senhor, sua idade é {}'.format(idade))
    else:
        if sexo == 'F' or sexo == 'f':
             print('Boa noite senhora, sua idade é {}'.format(idade))
        else:
            print('Opção inexistente!')
    idade = int(input('Digite sua idade: '))
print('Encerrando..')
