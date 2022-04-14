#Exercício para validar uma string a5LPA

def valida_string(frase, min, max):
    tam = len(frase)

    if ((tam < min) or (tam > max)):
        return False
        #Aqui vai avaliar como falso a condição que não atende o tamanho solicitado
    else:
        return True

#Programa principal
frase = input('Digite uma frase de 15 a 30 caracteres: ')
while valida_string(frase, 5, 30):
    frase = input('Digite uma frase de 15 a 30 caracteres: ')
print(frase)