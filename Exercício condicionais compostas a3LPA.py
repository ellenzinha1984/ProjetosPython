# Exercício 3.3.1
# Recebe nota de 3 matérias do aluno, verifica a média 7 e aprovação
n1 = float(input('Digite a nota da matéria 1: '))
n2 = float(input('Digite a nota da matéria 2: '))
n3 = float(input('Digite a nota da matéria 3: '))
if n1>=7 and n2>=7 and n3>=7:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')