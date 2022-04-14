# Exercício 2 prática 4 LPA - qtde cédulas para pagar um valor
# Valores inteiros e cédulas de R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 1

valor = int(input('Digite o valor R$ '))
# Precisaremos fazer algumas operações com if e else para contar quantas cédulas
# Verificarei quantas cédulas de cada "cabem" em cada valor - divisão de um valor pelo outro e pegar somente a parte inteira
# Verifico quantas cédulas e desconto do valor total
# While True fará com que apenas as condições desejadas sejam verificadas
while True:  # Loop infinito
    if (valor >= 100):
        cont100 = valor // 100  # Divisão pegando somente a parte inteira
        valor = valor - cont100 * 100  # Poderia ser aqui valor -= cont100 * 100
        print('Cédulas de 100: {}'.format(cont100))
        if not valor:  # Caso o valor seja 0, encerra o laço e ele não precisa fazer todos os testes (ex valor 500)
            break
    if (valor >= 50):
        cont50 = valor // 50  # Divisão pegando somente a parte inteira
        valor = valor - cont50 * 50
        print('Cédulas de 50: {}'.format(cont50))
        if not valor:
            break
    if (valor >= 20):
        cont20 = valor // 20  # Divisão pegando somente a parte inteira
        valor = valor - cont20 * 20
        print('Cédulas de 20: {}'.format(cont20))
        if not valor:
            break
    if (valor >= 10):
        cont10 = valor // 10  # Divisão pegando somente a parte inteira
        valor = valor - cont10 * 10
        print('Cédulas de 10: {}'.format(cont10))
        if not valor:
            break
    if (valor >= 5):
        cont5 = valor // 5  # Divisão pegando somente a parte inteira
        valor = valor - cont5 * 5
        print('Cédulas de 5: {}'.format(cont5))
        if not valor:
            break
    if valor:  # Aqui vai fazer apenas se sobrou alguma coisa
        cont1 = valor  #Aqui é apenas o que sobrar, não vou precisar fazer contas pois vai de um em um
        print('Cédulas de 1: {}'.format(cont1))
        break

