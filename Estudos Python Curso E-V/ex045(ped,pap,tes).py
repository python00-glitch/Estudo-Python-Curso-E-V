import random
from time import sleep

pedra = 0
papel = 1
tesoura = 2

materiais = [pedra, papel, tesoura]
escolhaPC = random.choice(materiais)

print("[0] = PEDRA \n[1] = PAPEL \n[2] = TESOURA")
print(15*"+")
escolhaU = int(input("Escolha um: "))
print("JO..")
sleep (0.5)
print("KEN..")
sleep(2)
print("PO!!")
print(escolhaPC)
print(15*"+")
if escolhaPC == pedra and escolhaU == pedra or escolhaPC == papel and escolhaU == papel or escolhaPC == tesoura and escolhaU == tesoura:
    print("EMPATE!")
elif escolhaPC == pedra and escolhaU == tesoura:
    print("VITÓRIA DA CPU!")
elif escolhaPC == papel and escolhaU == pedra:
    print("VITÓRIA DA CPU!")
elif escolhaPC == tesoura and escolhaU == papel:
    print("VITÓRIA DA CPU!")
elif escolhaU == pedra and escolhaPC == tesoura:
    print("VITÓRIA DA USUÁRIO!")
elif escolhaU == papel and escolhaPC == pedra:
    print("VITÓRIA DA USUÁRIO!")
elif escolhaU == tesoura and escolhaPC == papel:
    print("VITÓRIA DA USUÁRIO!")

input("Pressione 'Enter' para finalizar...")