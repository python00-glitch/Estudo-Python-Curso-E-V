# Faça um código que leia a frase do usuario, mostre-a ao contrario, e determine se ela é um palíndromo ou não
# (Palíndromos são frases que lidas do jeito que foram escritas, ou ao contrário, formam a mesma frase);
#
# O método '.upper' serve para que o computador entenda que toda string que for digitada pelo usuario se torne CapsLock
# para ele
#
# O método '.strip' elimina os espaços antes e depois de cada palavra;
#
# O método '.split' separa cada palavra digitada, como se fossem obejtos em uma lista, e as guarda dentro de coleções;
#       Exemplo: frase = str.split(input("cade o ovo")) // print(frase)
#       Terminal: 'cade', 'o', 'ovo';
#
# O método '.join' junta todas as strings que foram separadas. por isso, deve-se usar '.strip' logo na variavel para que
# o espaços não atrapalhem.
#
# 'len' significa que o método terá que usar o mesmo comprimento (que em inglês é 'length' = 'len') dos caracteres da
# outra variavel
#
# A variavel 'inverso' é a variavel que irá receber o loop negativo do 'for'
# Como irá funcionar a inversão usando numero negativo com o loop 'for':
#       (lembrando que 'for' é um loop em que nós determinamos quantas vezes ele irá se repetir, diferente do 'while',
#       que se repete infinatamente até ser interrompido por uma condição [if, else, True, False, etc], ou pelo 'break')
# Imaginemos uma frase: frase = "Bom dia."
# Esta frase ocupa espaço na memória do PC, e é guardada por caracteres.
# Então, quando ela for guardada, será distruida da seguinte forma: [0=B],[1=o],[2=m].['espaço'=3],[4=d],[5=i],[6=a],
# [7='.']
# Então, pela lógica, para vermos esta exata frase ao contrário, teriamos que usar o loop 'for' com numeros de condiçoes
# negativas
# Seguindo a lógica, os números seriam -7 e 0, que seriam do tamanho exato desta frase
# Mas não faria sentido para o computador, que teria que, primeiro, digitar a frase novamente ao contrario, e teriam
# casas vazias ocupando espaço no código, e isso traria erro na execução
# Por isso, usa-se os numeros -1, -1 e -1
# Começamos no primeiro "-1", que empurra a frase para o caractere -1 da fila
# O segundo "-1" é uma funçao que vai adicionando as letras em caracteres negativos
# E o terceiro "-1" se trata de uma barreira que implantamos na condição.
# Ficaria algo do tipo: 'for letra in range(len(frase) -1, -1)'
frase = str.upper(input("Digite uma frase e veja se ela é a mesma ao contrário (palíndromo): ")).strip() #elimina os espaços dentro da frase
separa = frase.split() #separa cada palavra que tinha espaço entre eles
junto = ''.join(separa) #junta todas as palavras, e como não existe mais espaços entre ela, elas viram uma só
print("A frase foi: {}".format(frase))
inverso = '' #fica nulo para receber a frase da variavel 'junto', e com as normas do loop c/ numero negativo, inverter a frase
for letra in range(len(junto)-1, -1, -1):
    inverso += junto
print("A frase ao contrário fica assim: {}".format(junto))
#if inverso == junto:
#    print("A sua frase É UM PALÍNDROMO!")
#else:
#    print("A sua frase NÃO É UM PALÍNDROMO!")