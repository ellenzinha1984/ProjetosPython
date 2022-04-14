# Variável que recebe nota do aluno e compara com a média
print('Variável que recebe nota do aluno e compara com a média')
print('Nota 5')
nota = 5
media = 7
resultado = nota >= media
print(resultado)
print('\n')
print('Nota 8')
nota = 8
media = 7
resultado = nota >= media
print(resultado)

print('\n')
print('\n')
print('\n')
print('\n')

# Exercício variável string concatenando com espaços repetidos
print('Exercício variável string concatenando com espaços repetidos')
frase = 'Python' + '-' * 5 + 'C' + '-' * 5 + 'Java' + '-' * 5 + 'PHP'
print(frase)
print('\n')
print('\n')
print('\n')

# Exercício variáveis combinadas em uma frase
print ('Exercício variáveis combinadas em uma frase - modo clássico')
comida = 'pizza'
ano = 1984
div = 1984 / (2021-1984)
frase = 'Minha comida preferida é %s, nasci em %i e a divisão do meu ano de nascimento pela minha idade é %.2f' % (comida, ano, div)
print(frase)
print('\n')
print ('Exercício variáveis combinadas em uma frase - modo moderno')
comida = 'pizza'
ano = 1984
div = 1984 / (2021-1984)
frase = 'Minha comida preferida é {}, nasci em {} e a divisão do meu ano de nascimento pela minha idade é {}' .format(comida, ano, div)
print(frase)
print('\n')
print('\n')
print('\n')

