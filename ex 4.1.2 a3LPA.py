# Exercício triângulos
l1 = float(input('Digite a medida l1 do triângulo: '))
l2 = float(input('Digite a medida l2 do triângulo: '))
l3 = float(input('Digite a medida l3 do triângulo: '))
if (l1==0 or l2==0 or l3==0):
    print('Este triângulo não existe pois um de seus lados tem medida 0!')
else:
    if (l3>l1 + l2 or l2>l1+l3 or l1>l2+l3):
        print('Este triângulo não existe pois a soma de dois de seus lados é maior que um dos seus lados')
    else:
        if (l1!=l2 and l1!=l3 and l2!=l3):
            print('Este triângulo é escaleno! Ele não possui nenhum lado igual.')
        else:
            if (l1==l2 and l1==l3):
                print('Este triângulo é equilátero! Seus 3 lados têm a mesma medida.')
            else:
                if (l1==l2 or l1==l3 or l2==l3):
                    print('Este triângulo é isósceles! Ele possui 2 lados iguais.')