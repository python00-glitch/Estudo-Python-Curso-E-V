import tkinter as tk
import pyautogui
import time
def executar_codigo():
    # Clica no botão 'windows'
    pyautogui.press("win")
    time.sleep(0.5)
    # Digite 'edge'
    pyautogui.write("edge")
    time.sleep(0.5)
    # Pressiona 'enter' no aplicativo do navegador 'Edge'
    pyautogui.press("enter")
    time.sleep(1)
    # Digite o link na barra de pesquisa
    pyautogui.write("https://web.whatsapp.com/")
    time.sleep(1)
    # Pressiona 'Enter' para pesquisar
    pyautogui.press("enter")
    time.sleep(15)
    # Clica na barra de pesquisa do whatsapp
    pyautogui.click(x=348, y=217)
    time.sleep(1)
    # Digita 'baby'
    pyautogui.write("baby")
    time.sleep(0.5)
    # Pressiona 'enter' para selecionar o contato
    pyautogui.press("enter")
    time.sleep(1)
    # Clica na barra de chat
    pyautogui.click(x=994, y=949)
    time.sleep(1)
    # Digita a mensagem
    pyautogui.write("boa noite, nenem :white")
    time.sleep(1)
    # Clica no pixel onde fica o emoji de 'coração branco'
    pyautogui.click(x=676, y=871)
    time.sleep(1)
    # Pressiona o 'enter' para enviar a mensagem
    pyautogui.press("enter")
    time.sleep(1)
    # Digita a mensagem
    pyautogui.write("dorme bem, baby, te amo muito muito :white")
    time.sleep(1)
    # Clica no emoji
    pyautogui.click(x=676, y=871)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    # Mais mensagem
    pyautogui.write(" fica com Deus, ate amanha, tchutchuca :white")
    time.sleep(2)
    # Clica no emoji
    pyautogui.click(x=676, y=871)
    time.sleep(1)
    # Pressiona 'enter' para enviar
    pyautogui.press("enter")
    time.sleep(5)
    # Pressiona 'alt+f4' para fechar o navegador
    pyautogui.hotkey("alt", "F4")

# Criação da janela
janela = tk.Tk()

# Título da janela
janela.title("BOA NOITE PARA NAMORADA")

# Dimensões da janela
janela.geometry("450x200")

# Rótulo para exibir instruções
label = tk.Label(janela, text="CLIQUE PARA MANDAR BOA NOITE PARA A NAMORADA")
label.pack(pady=20)

# Botão para executar o código
button = tk.Button(janela, text="BOA NOITE <3", command=executar_codigo)
button.pack()

# Iniciar loop de execução da interface
janela.mainloop()