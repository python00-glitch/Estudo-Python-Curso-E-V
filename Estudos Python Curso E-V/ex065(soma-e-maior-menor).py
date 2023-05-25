# Faça um software que some todos os numeros digitados, e mostre o maior e o menor deles, e pergunte se deseja continuar

maior = 0
menor = 0
lista = 0
while True:
    num = int(input("Digite um numero para ver a soma total dele: "))
    lista += num

    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    conf = str.upper(input("Deseja continuar? [S para sim] [N para não] "))
    if conf == 'S':
        continue
    else:
        break
print("")
print("O total de todos os valores é de {}".format(lista))
print("Enquanto isso, o maior numero digitado foi {} e o menor foi {}".format(maior, menor))
