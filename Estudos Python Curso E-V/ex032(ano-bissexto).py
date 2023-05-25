# Faça um software que leia o ano e diga se ele é bissexto ou não #
ano = int(input("Digite um ano e descubra se ele é bissexto: "))
if ano % 100 != 0 and ano % 4 == 0:
    print("Este ano é BISSEXTO!")
else:
    print("Este ano NÃO É BISSEXTO!")