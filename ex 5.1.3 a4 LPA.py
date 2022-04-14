# Exercício horas H:M:S

inicio = int(input('Digite a hora inicial (0 a 23h): '))
fim = int(input('Digite a hora final (0 a 23h - deve ser posterior à inicial): '))
cont = inicio
somahora = 0
while (inicio>fim) or (0 > inicio > 23) or (0 > fim > 23):
    # Aqui condiciona o laço a executar somente após o especificado para o dado digitado
    inicio = int(input('Digite a hora inicial (0 a 23h): '))
    fim = int(input('Digite a hora final (0 a 23h - deve ser posterior à inicial): '))
for h in range(inicio, fim + 1, 1):
    for m in range(0, 60, 1):
        for s in range(0, 60, 1):
            print(h,':',m,':',s,'h')
