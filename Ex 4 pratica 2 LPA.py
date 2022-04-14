print('Exercício frases e manipulação de strings')
frase = input('Digite uma frase qualquer: ')
tam = len(frase)
metade = frase[:int(tam/2)]  #aqui pegamos metade, mas tem que definir que é int
print(metade)
print(frase[-2:])  #- no índice indica que quero começar de trás para frente