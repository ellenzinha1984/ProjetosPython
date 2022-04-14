print('Condicionais simples em Phyton')
if (idade > 60):
    print('Você tem direito aos benefícios.')

if (dano > 10 and escudo == 0):  # ambas entradas devem ser verdadeiras no and
    print('Você está morto.')

if (norte == True or sul == True or leste == True or oeste == True):  # apenas uma variável true basta com o or
    print('Você escapou!')