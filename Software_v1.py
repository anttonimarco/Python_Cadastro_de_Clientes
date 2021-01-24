# Importação da biblioteca
from tkinter import *

# Declaração da variável para receber o TK
menu = Tk()

# Criação da classe e colocando a variável e loop dentro da classe, e assim personalizar.
class config():
    def __init__(self):
        self.menu = menu
        self.menuconfig()


        self.menu.mainloop()

    # Configuração do menu
    def menuconfig(self):
        self.menu.title('Cadastro de Clientes')
        self.menu.geometry('800x800+500+150')
        self.menu.resizable(True, True)
        self.menu.maxsize(height=850, width=850)
        self.menu.minsize(height=750, width=750)



config()