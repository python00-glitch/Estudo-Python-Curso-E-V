"Condição"

"os códigos sempre são executados de cima pra baixo, em sequencia"
"condiçoes em programaçao é quando sao colocadas dois caminhos para se seguir, e deve se decidir de acordo com o Fluxograma do código"
"no python, para definir um condiçao, usa-se as variaveis 'if', 'else', e 'elif' (que sera tratada mais para frente)"
"exemplo:"
nome = str(input("Digite seu nome: "))

if nome == "Ricardo":
    print("Bem-vindo, Sr. Ricardo.")
    input("Aperte Enter para prosseguir...")

tempo = int(input("Qual ano de fabricação do seu veículo: "))

if tempo <= 2013:
    print("Carro não elegível para o aplicativo.")
else:
    print("Ótimo!! Carro elegível para transporte!")
input("Aperte Enter para finalizar..")
print("FIM.")