# Faça um menu correspondente de algarismos
import time
while True:
    bv = "-----BEM VINDO-----"
    for letra in bv:
        print(letra, end="")
        time.sleep(0.3)
    print("")
    time.sleep(0.4)
    print("[1] Receitas para bolo de cenoura")
    time.sleep(0.4)
    print("[2] Receitas para doces gelados")
    time.sleep(0.4)
    print("[3] Receitas para hambúrgueres artesanais")
    time.sleep(0.4)
    print("[4] Receitas para cereias naturais feitos em casa")
    time.sleep(0.4)
    usuario = int(input("Por favor, escolha uma das opções acima: "))
    if usuario == 1:
        print("Você escolheu 'Receitas de Bolo de Cenoura', clique neste link:"
              "\nhttps://www.tudogostoso.com.br/receita/23-bolo-de-cenoura.html")

    elif usuario == 2:
        print("Você escolheu 'Receitas de Doces Gelados', clique neste link:"
              "\nhttps://www.tudogostoso.com.br/receita/144976-picole-de-manga.html")

    elif usuario == 3:
        print("Você escolheu 'Receitas de Hambúrgueres Artesanais', clique neste link:"
              "\nhttps://www.tudogostoso.com.br/receita/155011-hamburguer-caseiro.html")

    elif usuario == 4:
        print("Você escolheu 'Receitas de Cereais Naturais em Casa', clique neste link:"
              "\nhttps://www.thedishonhealthy.com/category/breakfast/page/2/")
    else:
        print("Opção inválida. Por favor, escolha uma das opções listadas abaixo.")
        continue

    opcao = str.upper(input("\nDigite 'S' para sair ou 'M' para voltar ao menu: "))
    if opcao == 'S':
        break
    elif opcao == 'M':
        continue
    else:
        print("Opção inválida. Por favor, escolha 'S' para sair ou 'M' para voltar ao menu.")