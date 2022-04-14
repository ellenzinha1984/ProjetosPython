#Exercício 1 prática 5 LPA - fatorial
#Fatorial é o número multiplicado pelos inteiros contidos nele
#Por exemplo fatorial de 5 - 5! = 5*4*3*2*1
#Fatorial de 0 é 1.
#Necessário validar dados
def valida_int(pergunta, min, max):  #Validação para digitar valor dentro do intervalo
    y = int(input(pergunta))  #recebe o valor a ser validado
    while ((y < min) or (y > max)):
        y = int(input(pergunta))
    return y

def fatorial(x):
    """
    Calcula a fatorial do número digitado
    :param x: número a ser calculado o fatorial
    :return: armazena o fatorial
    """
    fat = 1  #O menor valor de fatorial possível que existe é 1
    if x == 0:
        return fat  #Já faço uma verificação aqui para voltar 1 caso o valor seja 0
    #A partir daqui só vai ser executado se fatorial for maior que 1
    #Vou usar for porque sei o número de iterações que eu vou fazer
    for i in range(1,x + 1,1):  #limite é sempre o número + 1 para inclui-lo
        #Poderia fazer o passo começando do número digitado, mas aí teria que regredir
        #E o passo seria -1, limite seria 0
        fat *= i  #Isso é o mesmo que fat = fat * i
    return fat

#Programa principal
x = valida_int('Digite um valor a calcular fatorial: ',0,999999)
print('{}! = {}'.format(x,fatorial(x)))
help(fatorial)