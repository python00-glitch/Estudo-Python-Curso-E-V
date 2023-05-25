peso = 0
for c in range(1, 6):
    soma = int(input("Qual o peso da {}° pessoa: ".format(c)))
    peso += soma
    print("Até o momento, o total é {}: ".format(peso))