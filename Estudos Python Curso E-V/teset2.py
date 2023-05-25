import time

print("loading", end='')

num_reticencias = 3

#while True:
for i in range(2):
    for i in range(num_reticencias):
        print(".", end='', flush=True)
        time.sleep(0.3)

    for i in range(num_reticencias):
        print("\b \b", end='', flush=True)
        time.sleep(0.3)
print("")
print("carregamento completo!")
if str.upper(input("")) == 'RAYSSA':
            print("olá mundo!")

frase = 'me caguei nas calças'

for letra in frase:
    print(letra, end='', flush=True)
    time.sleep(0.1)

print()    
