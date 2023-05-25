import pyautogui
import time
import pandas as pd

# "pyautogui" é uma biblioteca de AUTOMAÇÃO, pesquise a documentação
# "pandas" é uma biblioteca que trabalha com BASE DE DADOS BRUTA
# Para reduzir o nome 'pandas' para escrever no código, escreve "import pandas as pd" para usar apenas 'pd'

# '.click()' clica com o mouse
# '.write()' escreve um texto
# '.press()' aperta UMA tecla em específico
# '.hotkey()' aperta um COMANDO específico de teclas
# '.PAUSE = ' (em maiúsculo) serve como o 'time.sleep'
    # exemplo: pyautogui.PAUSE = 0.5
# '.dragto()' arrasta até certo ponto da tela
# '.scroll()' scrolla a tela usando o scroll do mouse

# Para usar o '.click()', deve se saber a localização do mouse na tela
# Para isso, o código deste comando é 'pyautogui.click(x=, y=)', e na frente das letras, colocar a localização numerica
    # do mouse.
# Para saber a localização do mouse, usa-se o 'print(pyautogui.position())' e aparecerá a localização exata que deve-se
    # usar no comando.
# Um macete para descobrir a posição do mouse no local exato que voce precisa é usar o código 'print()' acima e colocando
    # um time.sleep de 5 segundos e deixando o mouse no local que precisa, depois dos 5 segundos aparecerá a posição
    # que voce precisa.
# Existe um PARÂMETRO do '.click()' chamado 'clicks= ', que voce define quantos cliques o mouse deve dar no local
    # indicado.
        # exemplo: 'pyautogui.click(x= 894, y= 465, clicks=2)
# Outro parâmetro para se usar no comando '.click()' é o 'button= ', que voce escolhe qual botão do mouse vai clicar
    # na automação.
        # exemplo: 'pyautogui.click(x= 894, y= 465, button="right")


# Para utilizar o "pandas" no código para ele ler uma base de dados, importe o "pandas" e o defina em uma variável
    # exemplo: tabela = pandas.read_pdf(arquivo.pdf)
# Em seguida, faça ele ler uma pasta do seu dispositivo ou online com 'pandas.read_{}()'
    # exemplo: (ler um caminho da pasta no dispositivo) 'pandas.read_pdf(r"C:\Users\user\Downloads\arquivo.pdf")
        # ('r' (raw) é um comando de print que faz com que o python ignore qualquer caractere especial no texto do caminho do local)
            # exemplos de caracteres especiais: \r, \t, \n
    # (nas chaves {} é o tipo de arquivo que deseja escolher para colocar nos parenteses, aperte "crtl + space")
    # (pode-se usar outros comandos dentro do "pandas.", para isso digite 'pandas.{}_{}()' )

tabela = pd.read_csv(r"C:\Users\rosel\OneDrive\Documentos\Estudos Intensivão Python\Compras.csv", sep=";")
print(tabela)
#pyautogui.press("win")
#time.sleep(0.5)
#pyautogui.write("edge")
#time.sleep(0.5)
#pyautogui.press("enter")
#time.sleep(0.5)
#pyautogui.write("youtube.com.br")
#time.sleep(0.5)
#pyautogui.press("enter")