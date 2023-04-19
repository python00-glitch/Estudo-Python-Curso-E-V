import random
print("Bem-vindo ao jogo da adivinhação! A CPU irá escolher um número aleatório de 1 á 5 \n Tente advinhar para ganhar o jogo.")
usuario = int(input("Digite um número: "))
n = [0, 1, 2, 3, 4, 5]
nr = random.choice(n)
print(nr)
if usuario != nr:
    print("Errou! Tente novamente...")
else:
    print("Acertou!!! Parabéns.")
input("Pressione Enter para finalizar/tentar novamente...")