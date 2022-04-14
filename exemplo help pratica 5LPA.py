# help(print)  Aqui ele mostra o help do print
# help()  Aqui ele mostra o help geral e permite que você digite a função

#Docstrings exemplo
def soma(x=0, y=0, z=0):
    """
    Função que soma até 3 valores inteiros
    :param x: valor inteiro opcional
    :param y: valor inteiro opcional
    :param z: valor inteiro opcional
    :return: soma inteiro
    """
    return x+y+z

print(soma(3,2))
help(soma)

#Tenho que criar uma docstring colocando três aspas e posso complementar
#Minha descrição

