#Busca de dados em uma lista a6LPA

def buscadado(lista, dado):
    x = 0  #Para definir a verificação do 0 que é o primeiro índice
    while x < len(lista):  #Aqui para fazer a verificação até o número total de itens da lista
        if (lista[x] == dado):  #Ele vai buscar de um em um a posição do dado que eu desejo
           return x
        x += 1
    return -1

#Programa
lista = [2, 4 , 6 , 8 , 10, 12, 14]
dado = int(input('Digite o número a ser buscado: '))
res = buscadado(lista,dado)  #Recebe a informação da lista e do dado a ser buscado
if res >=0: #Aqui a verificação é com 0 e -1, então se for 0 é pq encontrou e se for -1 é porque não encontrou, então foi pro else
    print('Dado {} foi encontrado na posição {}'.format(dado, res + 1))
else:
    print('Número não encontrado!')
