import time

print("loading", end= '')

# número de reticências que serão exibidas
num_reticencias = 3

# loop para exibir as reticências em um loop infinito
while True:
    # exibe as reticências
    for i in range(num_reticencias):
        print(".", end='', flush=True)
        time.sleep(0.3)

    # apaga as reticências
    for i in range(num_reticencias):
        print("\b \b", end='', flush=True)
        time.sleep(0.3)
if input() == '':
# frase que você deseja exibir
            print("olá mundo!")

# loop para iterar por cada caractere da frase
for letra in frase:
    # exibe a letra e espera 0,5 segundos antes de exibir a próxima
    print(letra, end='', flush=True)
    time.sleep(0.1)

# exibe uma nova linha depois que todas as letras foram exibidas
print()    
