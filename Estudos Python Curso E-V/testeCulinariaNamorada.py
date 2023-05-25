# Fazendo um programa para pegar itens dentro de uma lista, e atribuir ao loop for
# Neste caso, o programa vai pegar notas de uma pessoa sobre alguma comida, e tirar a média

# O 'i' (no 'for') representa á variáveis dentro da lista 'media' (no caso: s, c, g, e)
# O 'item' (no 'for') representa o valor das variáveis da lista 'media' (no caso: sabor, cheiro, gostosura, e. barriga)
# A funçao 'enumerate' é oque denomina essas duas coisas para ela mesma, e as chama para o loop

# Para obter a média de todas as notas, é precisa somar todas a notas, e depois dividir pela quantidade de notas somadas

# Para obter cor no python, agora, usamos o código ANSI com 'x1b', que funciona na mesma forma ('\x1b[m')

s = 'sabor'
c = 'cheiro'
g = 'gostosura'
e = 'enchimento de barriga'
m_nota = 0
media = [s, c, g, e]

for i, item in enumerate(media):
    nota = float(input("De \x1b[38;5;9m'0'\x1b[m á \x1b[38;5;70m'10'\x1b[m, "
                       "qual nota voce daria para \x1b[38;5;157m{}\x1b[m?".format(item)))
    print("Voce deu nota \x1b[38;5;37m{:.1f}\x1b[m para \x1b[38;5;37m'{}'\x1b[m.".format(nota, item))
    m_nota += nota

total_media = m_nota / 4
print("A média total para este alimento é \x1b[38;5;37m{:.2f}\x1b[m!".format(total_media))