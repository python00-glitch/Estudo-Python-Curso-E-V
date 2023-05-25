# Tentando fazer uma calculadora responsiva
import math

adic = '+'
sub = '-'
mult = '*'
div = '/'
pot = '**'
raiz = '///'
porc = '*/'

while True:
    try:
#        calculo = ' '.join(list(input("Digite um cálculo: ")))
#        n1, simb, n2 = calculo.split()
#        n1 = float(n1)
#        n2 = float(n2)
#        simb = str(simb)
        n1 = float(input("X: "))
        simb = str(input("X: "))
        if simb == '///':
            None
        else:
            n2 = float(input("X: "))
        if simb != adic or sub or mult or div or pot or raiz or porc    :
            raise ValueError("Digite um símbolo válido")
        if simb == adic:
            adic_r = n1 + n2
            print("A adição deu: {}".format(adic_r))
        elif simb == sub:
            sub_r = n1 - n2
            print("A subtração deu: {}".format(sub_r))
        elif simb == mult:
            mult_r = n1 * n2
            print("A multiplicação deu: {}".format(mult_r))
        elif simb == div:
            if n1 == 0 or n2 == 0:
                raise ValueError("Não existe divisão por 0 (ZERO)")
            else:
                div_r = n1 / n2
                print("A divisão deu: {:.1f}".format(div_r))
        elif simb == pot:
            pot_r = n1**n2
            print("A potênciação deu: {}".format(pot_r))
        elif simb == raiz:
            raiz_r = math.sqrt(n1)
            print("A raiz quadrada deu: {}".format(raiz_r))
        elif simb == porc:
            porc_r = n1 - (n1 * n2 / 100)
            print("O desconto foi de {:.0f}%, e sobrou: {}".format(n2, porc_r))
    except ValueError as error:
        c = input('{}! Tente novamente [Q], ou encerre [L]: '.format(error))
        if c == 'Q':
            continue
        elif c == 'L':
            break
