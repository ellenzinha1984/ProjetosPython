#Exercício para listar as linguagens de programação em tuplas

ling = ('Rust', 'TypeScript', 'Python', 'Kotlin', 'Go', 'Julia', 'Dart', 'Ce', 'Swift', 'JavaScript')
print('Top 10 Linguagens de Programação em 2020: ')
print('(segundo o Stack Overflow)')
for i in range(0, len(ling), 1):
    print(i+1,' - ', ling[i])  #Aqui imprime cada item da lista
print('\nO TOP 3: ',ling[3])  #Imprime o item 3 da tupla
print('Últimos 5: ',ling[-5:])  #Imprime os últimos 5 itens da tupla
i = 0
while (ling[i] != 'Python'):  #Aqui vamos testar a posição do Python na tupla
    i += 1
print('Pyton na posição {}'. format(i+1))