# Exercício borda palavra a5LPA
def borda(s1):
    tam = len(s1)
    # Agora vamos definir com o if que só imprima caso haja caracteres
    if tam:  # Aqui tam = true pois ele precisa ter conteúdo
        print('+','-' * tam,'+')  # Aqui eu multiplico o traço pelo num de caracteres
        print('|',s1,'|')
        print('+','-' * tam,'+')

# Programa principal
borda('Olá mundo!')
borda('Lógica de programação')
borda('')