#Exercício para armazenar dados de jogos e criar arquivo txt

def valida_int(pergunta, min, max):  #Validação para digitar valor dentro do intervalo
    y = int(input(pergunta))  #recebe o valor a ser validado
    while ((y < min) or (y > max)):
        y = int(input(pergunta))
    return y

def borda(s1):
        print('+','-' * 28,'+')  # Aqui eu multiplico o traço pelo num de caracteres
        print('|',s1,'|')
        print('+','-' * 28,'+')

def criaarquivo(nomearquivo):
    try:
        a = open(nomearquivo, 'wt+')  #w de write e t de arquivo tipo texto
        #Sinal de + cria arquivo caso ele não exista
        a.close()
    except:  #Erro genérico
        print('Erro na criação do arquivo.')
    else:
        print('Arquivo {} criado com sucesso!\n'.format(nomearquivo))

def existe_arquivo(nomearquivo):  #Verifica se arquivo existe
    try:  #Tenta fazer algo, e se tiver sucesso faz senão faz except
        a = open(nomearquivo, 'rt')  #r de read e t de arquivo de texto
        a.close()
        #Se acontecer erro na abertura ou fechamento, ocorre except
    except FileNotFoundError:  #Erro para arquivo não conseguir abrir
        return False
    else:
        return True  #Se deu certo é true

def cadastrarjogo(nomearquivo, nomejogo, nomeconsole):
    try:  #Como vou manipular arquivo, fazer try
        a = open(nomearquivo, 'at')  #a abre o arquivo, escreve mas mantém conteúdo
    except:
        print('Erro ao abrir o arquivo.')
    else:
        a.write('{};{}\n'.format(nomejogo,nomeconsole))  #Variáveis locais
    finally:  #Dando erro ou não, preciso fechar o arquivo
        a.close()

def listaarquivo(nomearquivo):
    try:
        a = open(nomearquivo, 'rt')  #r apenas abre arquivo para leitura
    except:
        print('Erro ao ler o arquivo.')
    else:
        print(a.read())  #Print na tela de todos os dados no arquivo
    finally:
        a.close()
#Programa principal
arquivo = 'games.txt'  #Cria um arquivo
if existe_arquivo(arquivo):  #True
    print('Arquivo localizado no computador.')
else:
    print('Arquivo inexistente.')
    criaarquivo(arquivo)

#Função que verifica se arquivo já existe e vou usar ele
#Ou arquivo existe e eu uso e edito, ou se não existe eu crio o arquivo
while True:  #Loop infinito pois não sei qtos jogos tem
    borda('            MENU            ')
    print('|',' ','1 - Cadastrar novo item ',' ','|')
    print('|', ' ','2 - Listar cadastros    ', ' ', '|')
    print('|', ' ','3 - Sair                ', ' ', '|')
    print('+------------------------------+')
    op = valida_int('Digite a opção: ',1,3)
    if op ==1:
        print('Opção de cadastrar novo item selecionada...\n')
        nomejogo = input('Nome do jogo: ')
        nomeconsole = input('Console: ')
        cadastrarjogo(arquivo, nomejogo, nomeconsole)
    elif op==2:
        print('Opção de listar itens selecionada...\n')
        listaarquivo(arquivo)
    elif op==3:
        print('Encerrando o programa...')
        break
