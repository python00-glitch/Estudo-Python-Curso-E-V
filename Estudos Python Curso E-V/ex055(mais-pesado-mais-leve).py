# Faça um programa que leia 5 pesos e mostre quem é a mais pesada, e quem é a mais leve
from time import sleep
maior_peso = 0
menor_peso = 0
c_sexo = 0
maior_sexo = ''
menor_sexo = ''
maior_nome = ''
menor_nome = ''
for p in range(1, 3):
    nome = str.upper(input("Digite seu nome: "))
    sexo = int(input("Digite [1] se voce é HOMEM e [2] se você é MULHER: "))
    if sexo == 1:
        c_sexo = 'dele'
    elif sexo == 2:
        c_sexo = 'dela'
    peso = float(input("Você é a {}º pessoa da pesquisa. Por favor, digite seu peso a seguir: ".format(p)))
    if p == 1:
        maior_peso = peso
        menor_peso = peso
        maior_nome = nome
        menor_nome = nome
    else:
        if peso > maior_peso:
            maior_peso = peso
            maior_nome = nome
            maior_sexo = c_sexo
        if peso < menor_peso:
            menor_peso = peso
            menor_nome = nome
            menor_sexo = c_sexo
print("")
agrad = "Muito obrigado pela sua participação na nossa pesquisa! Até breve."
for letra in agrad:
    print(letra, end='')
    sleep(0.05)
for letra in range(len(agrad)):
    print("\b \b", end='', flush=True)
    sleep(0.005)
print("")
print("")
print("{} é a pessoa com o MAIOR PESO registrado. O peso {} é de {}kg. ".format(maior_nome, maior_sexo, maior_peso))
sleep(1)
print("{} é a pessoa com o MENOR PESO registrado. O peso {} é de {}kg. ".format(menor_nome, menor_sexo, menor_peso))