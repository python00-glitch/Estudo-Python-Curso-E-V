# Faça um programa que leia os numeros do usuario e, quando ser digitado 999, o programa some os numero sem contar o 999

alg = 0
while True:
    num = int(input("Escreva um algarismo: "))
    if num == 999:
        break
    else:
        alg += num
print(alg)