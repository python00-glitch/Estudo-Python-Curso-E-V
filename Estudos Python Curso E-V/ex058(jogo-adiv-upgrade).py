# Faça um jogo melhorado do exercicio 028, mas agora toda vez que o usuario errar, ele deverá tentar novamente
# E deverá mostrar no final a contabilizaçao de todas as tentativas
import random
import time

print("Bem-vindo ao jogo da adivinhação! A CPU irá escolher um número aleatório de 1 á 10 \nTente advinhar para ganhar o jogo.")
erros = 0
#n = [0, 1, 2, 3, 4, 5]   |--- modelos que ocupavam
#nr = random.choice(n)    |--- mais linhas.
nr = random.randint(1,10)
usuario = int(input("\nDigite um número (cheat ({}): ".format(nr)))
while usuario != True:
    if usuario == nr:
        usuario = True
        print("\nAcertou!!! O seu número escolhido foi {}, e o número escolhido pela CPU foi {}. Parabéns.".format(usuario, nr))
        print("Foram {} tentativas até a vitória!".format(erros))
        print("")
        reiniciar = str.upper(input("Deseja JOGAR NOVAMENTE [Pressione 'C'] ou SAIR [Pressione 'S']: "))
        if reiniciar == 'C':
            print("\nComeçando novamente", end='')
            num = 3
            for c in range(2):
                for i in range(num):
                    print(".", end='', flush=True)
                    time.sleep(0.3)

                for t in range(num):
                    print("\b \b", end='', flush=True)
                    time.sleep(0.3)
            print("")
            continue
        elif reiniciar == 'S':
            print("\nJogo encerrado após VITÓRIA")
            break

    if usuario != nr:
        usuario = False
        erros += 1
        if usuario < nr:
            print("Mais...")
        elif usuario > nr:
            print("Menos...")
        conf = str.upper(input("Está errado! Por favor, [Pressione 'C'] para CONTINUAR,"
                               " ou [Pressione 'S'] para SAIR: "))
        if conf == 'S':
            print("\nJogo encerrado por DESISTÊNCIA")
            #break
            #exit()
            quit()
        elif conf == 'C':
            print("\nRetomando", end='')
            num = 3
            for c in range(1):
                for i in range(num):
                    print(".", end='', flush=True)
                    time.sleep(0.3)

                for i in range(num):
                    print("\b \b", end='', flush=True)
                    time.sleep(0.3)
                print("")
                usuario = int(input("\nDigite um número (cheat ({}): ".format(nr)))


