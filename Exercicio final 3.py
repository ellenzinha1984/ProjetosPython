#Atividade 3 - Lógica de Programação e Algoritmo

def dimensoesObjeto():  #Função para cálculo das dimensões do objeto e do valor de acordo com a dimensão
    while True:  #Laço para loop infinito até que alguma condição abaixo seja atendida
        try:  #Para podermos avaliar a execução do código e possíveis exceções (Está dentro do while para dar continue em caso de dado inválido
            alt = float(input('Digite a altura do objeto: '))  #Recebe a altura do objeto
            comp = float(input('Digite o comprimento do objeto: '))  #Recebe o comprimento do objeto
            larg = float(input('Digite a largura do objeto: '))  #Recebe a largura do objeto
            global volumeObjeto  #Variável definida como global para ser utilizada posteriormente
            volumeObjeto = alt * larg * comp  #Cálculo do volume do objeto
            if volumeObjeto < 1000:  #Início das verificações do volume para recebimento do valor de acordo com as dimensões
                valordimensoes = 10 #Recebe o valor do multiplicador para cada dimensão a seguir
                return valordimensoes  #Vai retornar o valor da variável valordimensoes na função dimensoesObjeto e encerra o laço
            elif volumeObjeto >= 1000 and volumeObjeto < 10000:
                valordimensoes = 20
                return valordimensoes
            elif volumeObjeto >= 10000 and volumeObjeto < 30000:
                valordimensoes = 30
                return valordimensoes
            elif volumeObjeto >= 30000 and volumeObjeto < 100000:
                valordimensoes = 50
                return valordimensoes
            else:  #Esse else obriga o usuário a digitar uma dimensão dentro das aceitas e recomeça o laço
                print('Objeto com dimensões maiores que às aceitas (maior que 100000 cm3).')
                print('Entre com as dimensões novamente!')
                continue
        except ValueError:  #Ocorre em tempo de execução, se valor digitado não for numérico decimal (float) recomeça laço
            print('Digite uma dimensão válida (numérica).')
            continue


def pesoObjeto():  #Função para definição do multiplicador conforme o peso do objeto
    while True:  #Laço infinito para podermos receber peso válido e depois definir o multiplicador
        try:  # Para podermos avaliar a execução do código e possíveis exceções
            global peso  #Variável definida como global para ser utilizada posteriormente
            peso = float(input('Digite o peso do objeto em kg: '))  #Recebe o peso
            if peso > 0 and peso < 0.1:  #Início das verificações das faixas de peso para definição do multiplicador
                valorPeso = 1
                return valorPeso  #Vai retornar o valor da variável valorPeso na função pesoObjeto e encerra o laço
            elif peso >= 0.1 and peso < 1:
                valorPeso = 1.5
                return valorPeso
            elif peso >= 1 and peso < 10:
                valorPeso = 2
                return valorPeso
            elif peso >= 10 and peso < 30:
                valorPeso = 3
                return valorPeso
            else:  #Esse else obriga o usuário a digitar um peso dentro do permitido, caso contrário recomeça laço
                print('Objeto com peso maior que o aceito (acima de 30 kg) ou peso nulo.')
                print('Entre com um peso permitido:')
                continue
        except ValueError:  #Ocorre em tempo de execução, se valor digitado não for numérico decimal (float) recomeça laço
            print('Digite um peso válido (numérico).')
            continue

def rotaObjeto():  #Função para definição de valor conforme a rota
    while True:  #Laço infinito para podermos receber rota válida e depois definir o multiplicador
        global rota  #Variável definida como global para ser utilizada posteriormente
        print('Rotas disponíveis para o objeto:\nRS - Rio de Janeiro a São Paulo\nSR - São Paulo a Rio de Janeiro\nBS - Brasília a São Paulo\nSB - São Paulo a Brasília\nBR - Brasília a Rio de Janeiro\nRB - Rio de Janeiro a Brasília')
        rota = input('Escolha a rota desejada: ')  #Variável para receber a rota
        if rota == 'RS' or rota == 'rs' or rota == 'SR' or rota == 'sr': #Início das verificações das rotas para definição do multiplicador
            valorRota = 1
            return valorRota  #Vai retornar o valor da variável valorRota na função rotaObjeto e encerra o laço
        elif rota == 'BS' or rota == 'bs' or rota == 'SB' or rota == 'sb':
            valorRota = 1.2
            return valorRota
        elif rota == 'BR' or rota == 'br' or rota == 'RB' or rota == 'rb':
            valorRota = 1.5
            return valorRota
        else:  #Aqui se for digitado qualquer valor diferente dos verificados acima ele recomeça o laço para receber a rota
            print('Rota inválida. Escolha uma das rotas disponiveis!')
            continue

#------------------  Início do código do programa principal ----------------------------
print('Bem vindo ao Centro de Logística Ellen Canossa Gagliardi Murata')  #Identificador pessoal - meu RU é 3967495
dimensoes = dimensoesObjeto()  #Variável que recebe valor retornado na função dimensoesObjeto
print('Objeto tem {} cm3'.format(volumeObjeto))  #Retorna o volume do objeto armazenado na variável global volumeObjeto
print('Valor para essas dimensões: R${:.2f}\n'.format(dimensoes))
multiplicapeso = pesoObjeto()  #Variável que recebe valor retornado na função pesoObjeto
print('O objeto tem {} kg'.format(peso))  #Retorna o peso do objeto armazenado na variável global peso
print('Multiplicador do objeto: {:0}\n'.format(multiplicapeso))
multiplicarota = rotaObjeto()  #Variável que recebe valor retornado na função rotaObjeto
print('A rota escolhida foi {}'.format(rota))  #Retorna o valor armazenado na variável rota global (rota escolhida)
print('Multiplicador para a rota: {:0}\n'.format(multiplicarota))
totalfrete = dimensoes * multiplicapeso * multiplicarota  #Cálculo do do total do transporte
print('Para o objeto com {} cm3, peso {}kg, para a rota {} o total a pagar pelo transporte é: R${:.2f}'.format(volumeObjeto, peso, rota,totalfrete))