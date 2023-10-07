#Questão 1
def soma(x, y):
    result = x + y
    return result


#Questão 2
def quadrado(x):
    result = x * 0.5
    return result


#Questão 3
def impar_par(x):
    if x % 2 == 0:
        return 'O número {} é par'.format(x)
    else:
        return'O número {} é impar'.format(x)


#Questão 4
def posi_neg(x):
    if x > 0:
        return 'O número {} é positivo'.format(x)
    elif x == 0:
        return 'O número é {}'.format(x)
    else:
        return 'O número {} é negativo'.format(x)


#Questão 5
def fatorial(x):
    if x == 0:
        return 1
    else:
        return x * fatorial(x-1)


#Questão 6
def primo(x):
    y = 1
    z = 0
    while y <= x:
        if x % y == 0:
            z = z + 1
        y = y + 1
    if z == 2:
        return 'O número {} é primo'.format(x)
    else:
        return 'O número {} não é primo'.format(x)   


#Questão 7
def converte(x):
    x = x * 1.8 + 32
    return x

#Questão 8
def km_m(x):
    while True:
        x = x / 3.6
        return x

#Questão 9
def hora_num(x):
    x = x * 60
    return x 

#Questão 10
def idade(x):
    if x >= 18:
        return 'Pode comprar bebida'
    elif x >= 16 and x < 18:
        return 'Pode comprar com permissão dos pais'
    elif x < 16:
        return 'Não pode comprar bebida'

#Questão 11
def maior(x, y):
    if x > y:
        return "{} é maior do que {}".format(x, y)
    elif y > x:
        return '{} é maior do que {}'.format(y, x)

#Questão 12
def mdc(x, y):
    while y > 0:
        x, y = y, x % y
    return x
