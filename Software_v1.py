# OBS> Seguir regra PEP 8
from tkinter import *  # Importação da biblioteca


menu = Tk()  # Declaração da variável para receber o TK


class menu_cadastro:  # Criação da classe.
    def __init__(self):
        self.menu = menu
        self.menucadastro()
        self.textomenu()
        self.entradadados()
        self.botoes()
        self.menu.mainloop()


    def menucadastro(self):  # Configuração do menu
        self.menu.title('Cadastro de Clientes')
        self.menu.geometry('700x700+600+150')
        self.menu.resizable(True, True)
        self.menu.maxsize(height=800, width=800)
        self.menu.minsize(height=600, width=600)
        self.menu.configure(background='#CCFFFF')

        self.quadrado1 = Frame(self.menu, background='#00CCFF', highlightbackground='#3399FF', highlightthickness=3,
                               bd=5)  # Criacão de um quadrado para dar um acabamento.
        self.quadrado1.place(relx=0.04, rely=0.05, relheight=0.55, relwidth=0.92)

    def textomenu(self):  # Criação textos no menu.
        self.txt_codigo = Label(self.menu, text='Código', background='#CCFFFF')
        self.txt_codigo.place(relx=0.10, rely=0.20, relheight=0.05, relwidth=0.10)

        self.txt_nome = Label(self.menu, text='Nome',bg='#00CCFF', background='#CCFFFF')
        self.txt_nome.place(relx=0.10, rely=0.30, relheight=0.05, relwidth=0.10)

        self.txt_telefone = Label(self.menu, text='Telefone', background='#CCFFFF')
        self.txt_telefone.place(relx=0.10, rely=0.40, relheight=0.05, relwidth=0.10)

        self.txt_cidade = Label(self.menu, text='Cidade', background='#CCFFFF')
        self.txt_cidade.place(relx=0.10, rely=0.50, relheight=0.05, relwidth=0.10)

    def entradadados(self):  # Criação dos campos da entrada de dados.
        self.entrada_codigo = Entry(self.menu)
        self.entrada_codigo.place(relx=0.21, rely=0.20, relheight=0.05, relwidth=0.15)

        self.entrada_nome = Entry(self.menu)
        self.entrada_nome.place(relx=0.21, rely=0.30, relheight=0.05, relwidth=0.68)

        self.entrada_telefone = Entry(self.menu)
        self.entrada_telefone.place(relx=0.21, rely=0.40, relheight=0.05, relwidth=0.68)

        self.entrada_cidade = Entry(self.menu)
        self.entrada_cidade.place(relx=0.21, rely=0.50, relheight=0.05, relwidth=0.68)

    def botoes(self):  # Criação dos botões.
        self.botao_limpar = Button(self.menu, text='Limpar', border=5)
        self.botao_limpar.place(relx=0.15, rely=0.10, relheight=0.06, relwidth=0.10)

        self.botao_buscar = Button(self.menu, text='Buscar', border=5)
        self.botao_buscar.place(relx=0.30, rely=0.10, relheight=0.06, relwidth=0.10)

        self.botao_novo = Button(self.menu, text='Novo', border=5)
        self.botao_novo.place(relx=0.45, rely=0.10, relheight=0.06, relwidth=0.10)

        self.botao_alterar = Button(self.menu, text='Alterar', border=5,)
        self.botao_alterar.place(relx=0.60, rely=0.10, relheight=0.06, relwidth=0.10)

        self.botao_apagar = Button(self.menu, text='Apagar', border=5)
        self.botao_apagar.place(relx=0.75, rely=0.10, relheight=0.06, relwidth=0.10)


menu_cadastro()