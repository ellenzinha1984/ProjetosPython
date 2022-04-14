#Exercício nota aluno lista a6 LPA
try:
    notas = []
    while (x >=0):
        notas.append(x)  #Aqui vou adicionando as notas recebidas em x na lista "notas"
        x = float(input('Digite uma nota: '))
    soma = 0  #Aqui vou criar uma variável para somar as notas e poder depois calcular a média
    for i in notas:  #varro as notas da lista
        soma += i  #Aqui vou somando as notas conforme ele varre a lista. Tem que ser a variáver da contagem!!
    media = soma/len(notas)
    print(notas)
    print('Média das notas digitadas: {:.2f} '.format(media))
except ZeroDivisionError:
    print('Nenhum valor foi digitado para o cálculo! Encerrando...')  #Aqui caso nenhuma nota válida seja digitada


