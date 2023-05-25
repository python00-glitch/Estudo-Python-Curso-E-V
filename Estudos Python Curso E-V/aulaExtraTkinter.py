from tkinter import *

# Tk() é um código da biblioteca Tkinter que cria a janela da interface gráfica
janela = Tk()
# Editamos o título da janela
janela.title("TESTE INTERFACE GRÁFICA")

# Label é um código de texto que colocamos na janela
# Dentro das suas condicoes, precisamos definir qual 'Tk' (qual janela) devemos coloca-la, e qual o texto escolhido
texto = Label(janela, text="TESTE TESTE TESTE TESTE")
# Em '.grid' escolhemos qual coluna e linha colocamos a variavel escolhida
# Nós definimos quantas colunas e linhas temos na interface, podendo dividi-la em várias, mas nao podemos pular
    # exemplo: "column=1" e depois colocar outro grid com "column=3"
texto.grid(column=0, row=0)

texto2 = Label(janela, text="TESTE2 TESTE2 TESTE2 TESTE2")
texto2.grid(column=0, row=1)

# .'mainloop' deixa a interface grafica ativa enquanto nao a fechamos
janela.mainloop()