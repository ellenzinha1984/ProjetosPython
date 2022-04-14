#Exercício string e números em tupla a6 LPA

def maior(msg, *num):  #Como vão ser vários números tem que ter *
    maior = 0
    for i in range(0, len(num), 1):
        if(num[i]) > maior:
            maior = num[i]
    print(msg, maior)

#Programa
maior('Maior: ',8,6,4,78,56,20,40,70,1)