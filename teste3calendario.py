import calendar
from tkinter import *

# Definir o ano e mês
ano = 2025
mes = 3

# Criar o calendário para o mês especificado
calendario = calendar.month(ano, mes)

# Criar a janela de saída
janela = Tk()
janela.geometry('500x300')
janela.title('Calendário de Março de 2025')

# Adicionar o calendário à janela
calendario_label = Label(janela, text=calendario, font=('Comic Sans', 28))
calendario_label.pack()

# Iniciar a janela
janela.mainloop()
