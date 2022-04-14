#Atividade 4 - Lógica de Programação e Algoritmo
listaPecas = []  #Variável da lista será global para poder ser utilizada em qualquer parte do código

#Início função cadastrarPeca para cadastro das peças
def cadastrarPeca(codigo):  #Função para cadastro das peças
    print('** CADASTRO DE PEÇAS **')
    print('Código da peça a ser cadastrada: {:0}'.format(codigo))
    nome = input('Nome da peça: ')  #Variável para receber o nome da peça
    fabricante = input('Fabricante da peça: ')  #Variável para receber o fabricante da peça
    valor = float(input('Valor da peça em R$: '))  #Variável para receber o valor da peça
    #A seguir criação do dicionário onde serão definidos os valores a serem armazenados
    dicionarioPecas = {'codigo' : codigo,
                       'nome' : nome,
                       'fabricante' : fabricante,
                       'valor' : valor}
    listaPecas.append(dicionarioPecas.copy())  #Farei cópia dos dados inseridos acima no dicionarioPecas na listaPecas
#Fim da função cadastrarPeca
#----------------------------------------------------------------
#Início da função consultarPeca
def consultarPeca():  #Função para consulta de peças da lista
    while True:  #Loop infinito para indefinidas consultas
        try:  #Try para evitar inserção de valores para consulta que possam gerar exceções
            print('** CONSULTA DE PEÇAS **')
            print('Consultas disponíveis:')
            print('1 - Consultar todas as peças\n2 - Consultar peças por código\n3 - Consultar peças por fabricante\n4 - Retornar')
            consulta = int(input('Digite a opção desejada: '))
            if consulta == 1:  #Aqui será a listagem de todos os itens
                print('Listagem de todas as peças')
                #Verificação de cada item de peça da listaPecas, que é na verdade conjunto de infos do dicionário inserido na lista:
                for pecas in listaPecas: #Seleciona cada dicionário cadastrado na listaPecas
                    for key, value in pecas.items():  #Para cada conjunto de campos do dicionário na listaPecas eu retorno os valores
                        print('{} : {}'.format(key, value))
            elif consulta == 2:  #Aqui será a consulta por código
                print('Consulta por código')
                digitacod = int(input('Digite o código a ser buscado: '))  #Variável que recebe o código digitado pelo usuário
                for pecas in listaPecas:  #Seleciona cada dicionário cadastrado na listaPecas
                    if pecas['codigo'] == digitacod:  #Faço a busca do código desejado na listaPecas
                        for key, value in pecas.items():  #Para cada conjunto de valores correspondentes na listaPecas eu retorno os valores
                            print('{} : {}'.format(key, value))
            elif consulta == 3:  #Aqui será a consulta por fabricante
                print('Consulta por fabricante')
                digitafabricante = input('Digite o fabricante a ser buscado: ')  #Variável que recebe o fabricante digitado pelo usuário
                for pecas in listaPecas:  #Seleciona cada dicionário cadastrado na listaPecas
                    if pecas['fabricante'] == digitafabricante:  #Faço a busca do fabricante desejado na listaPecas
                        for key, value in pecas.items():  #Para cada conjunto de valores correspondentes na listaPecas retorno os valores
                            print('{} : {}'.format(key, value))
            elif consulta == 4:
                print('Retornando ao menu anterior...')
                break  #Encerra o laço da função
            else:  #Caso usuário digite uma opção não disponível
                print('Digite uma opção válida!')
                continue
        except ValueError:  #Caso usuário digite valor que gere erro
            print('Digite uma opção válida!')
            continue
#Fim da função consultarPeca
#---------------------------------------------------------------
#Início da função removerPeca
def removerPeca():  #Função para remoção de cadastro de peça com base no código
    print('** REMOÇÃO DE REGISTRO DE PEÇAS **')
    remocao = int(input('Digite o código a ser excluído: '))  #Recebe o código a ser consultado e excluído
    for pecas in listaPecas:  #Seleciona cada dicionário cadastrado na listaPecas
        if pecas['codigo'] == remocao:  # Faço a busca do fabricante desejado na listaPecas
            listaPecas.remove(pecas)  #remove o registro referente ao código digitado
#Fim da função removerPeca


#------------------  Início do código do programa principal----------------------------
print('BEM-VINDO À BICICLETARIA DA ELLEN CANOSSA GAGLIARDI MURATA')  #Identificador pessoal - meu RU é 3967495
cod = 0  #Variável para receber o código das peças e ir "auto incrementando"
while True:  #Laço infinito pois não sei quantas peças serão cadastradas, e para validar escolha do menu
    try:  #Try para evitar inserção de valores de opção que possam gerar exceções
        print('** CONTROLE DE ESTOQUE DA BICICLETARIA **')
        print('Opções disponíveis:')
        print('1 - Cadastrar peça\n2 - Consultar peça\n3 - Remover peça\n4 - Sair')
        opcao = int(input('Escolha a opção desejada: '))
        if opcao == 1:  #Os if e elif farão a verificação de código escolhido para chamar a função correspondente
            cod += 1  #Aqui vamos incrementando automaticamente o valor do código conforme as peças são cadastradas
            cadastrarPeca(cod)  #Chama a função cadastrarPeca com atributo do código auto incrementado.
        elif opcao == 2:
            consultarPeca()  #Chama a função consultarPeca
        elif opcao == 3:
            removerPeca()  #Chama a função removerPeca
        elif opcao == 4:
            print('Encerrando o programa...')
            print('Até logo!')
            break  #Encerramento do loop e consequentemente do programa
        else:  #Aqui caso o usuário não digite uma opção disponível
            print('Digite uma opção válida!')
            continue  #Retorna para o início do laço
    except ValueError:  #Caso usuário digite valor que gere erro
        print('Digite uma opção válida!')
        continue  #Retorna para o início do laço
