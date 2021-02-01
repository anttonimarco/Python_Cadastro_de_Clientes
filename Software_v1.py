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
        self.menu.geometry('800x800+600+150')
        self.menu.resizable(True, True)
        self.menu.maxsize(height=800, width=800)
        self.menu.minsize(height=600, width=600)
        self.menu.configure(background='#CCFFFF')

        self.quadrado1 = Frame(self.menu, background='#00CCFF', highlightbackground='#3399FF', highlightthickness=3,
                               bd=5)  # Criação de um Frame (área retangular)
        self.quadrado1.place(relx=0.04, rely=0.05, relheight=0.89, relwidth=0.92)

        self.testimagem = Frame(self.menu, background='yellow')
        self.testimagem.place(relx=0.09, rely=0.10, relheight=0.20, relwidth=0.15)

    def textomenu(self):  # Criação textos no menu.
        self.txt_codigo = Label(self.menu, text='Código', background='#00CCFF')
        self.txt_codigo.place(relx=0.25, rely=0.08, relheight=0.05, relwidth=0.10)

        self.txt_nome = Label(self.menu, text='Nome', bg='#00CCFF', background='#00CCFF')
        self.txt_nome.place(relx=0.46, rely=0.08, relheight=0.05, relwidth=0.10)

        self.txt_cpf_cnpj = Label(self.menu, text='CPF/CNPJ', bg='#00CCFF', background='#00CCFF')
        self.txt_cpf_cnpj.place(relx=0.26, rely=0.15, relheight=0.05, relwidth=0.10)

        self.txt_rg = Label(self.menu, text='RG', bg='#00CCFF', background='#00CCFF')
        self.txt_rg.place(relx=0.45, rely=0.15, relheight=0.05, relwidth=0.10)

        self.txt_estado_civil = Label(self.menu, text='Estado Civil', bg='#00CCFF', background='#00CCFF')
        self.txt_estado_civil.place(relx=0.70, rely=0.15, relheight=0.05, relwidth=0.10)

        self.txt_data_nascimento = Label(self.menu, text='Data nascimento', bg='#00CCFF', background='#00CCFF')
        self.txt_data_nascimento.place(relx=0.27, rely=0.22, relheight=0.05, relwidth=0.13)

        self.txt_sexo = Label(self.menu, text='Sexo', bg='#00CCFF', background='#00CCFF')
        self.txt_sexo.place(relx=0.44, rely=0.22, relheight=0.05, relwidth=0.13)

        self.txt_profissao = Label(self.menu, text='Profissão', bg='#00CCFF', background='#00CCFF')
        self.txt_profissao.place(relx=0.68, rely=0.22, relheight=0.05, relwidth=0.13)

        self.txt_endereco = Label(self.menu, text='Endereço', bg='#00CCFF', background='#00CCFF')
        self.txt_endereco.place(relx=0.25, rely=0.29, relheight=0.05, relwidth=0.13)

        self.txt_numero = Label(self.menu, text='Numero', bg='#00CCFF', background='#00CCFF')
        self.txt_numero.place(relx=0.68, rely=0.29, relheight=0.05, relwidth=0.13)

        self.txt_complemento = Label(self.menu, text='Complemento', bg='#00CCFF', background='#00CCFF')
        self.txt_complemento.place(relx=0.26, rely=0.36, relheight=0.05, relwidth=0.13)

        self.txt_bairro = Label(self.menu, text='Bairro', bg='#00CCFF', background='#00CCFF')
        self.txt_bairro.place(relx=0.57, rely=0.36, relheight=0.05, relwidth=0.13)

        self.txt_cep = Label(self.menu, text='CEP', bg='#00CCFF', background='#00CCFF')
        self.txt_cep.place(relx=0.05, rely=0.43, relheight=0.05, relwidth=0.13)

        self.txt_uf = Label(self.menu, text='UF', bg='#00CCFF', background='#00CCFF')
        self.txt_uf.place(relx=0.32, rely=0.43, relheight=0.05, relwidth=0.13)

        self.txt_cidade = Label(self.menu, text='Cidade', background='#00CCFF')
        self.txt_cidade.place(relx=0.63, rely=0.43, relheight=0.05, relwidth=0.10)

        self.txt_telefone = Label(self.menu, text='Telefone', background='#00CCFF')
        self.txt_telefone.place(relx=0.08, rely=0.50, relheight=0.05, relwidth=0.10)

        self.txt_celular = Label(self.menu, text='Celular', background='#00CCFF')
        self.txt_celular.place(relx=0.35, rely=0.50, relheight=0.05, relwidth=0.10)

        self.txt_email = Label(self.menu, text='E-Mail', background='#00CCFF')
        self.txt_email.place(relx=0.63, rely=0.50, relheight=0.05, relwidth=0.10)

        self.txt_observacao = Label(self.menu, text='Observações', background='#00CCFF')
        self.txt_observacao.place(relx=0.09, rely=0.58, relheight=0.05, relwidth=0.10)

    def entradadados(self):  # Criação dos campos da entrada de dados.
        self.entrada_codigo = Entry(self.menu)
        self.entrada_codigo.place(relx=0.27, rely=0.12, relheight=0.03, relwidth=0.20)

        self.entrada_nome = Entry(self.menu)
        self.entrada_nome.place(relx=0.49, rely=0.12, relheight=0.03, relwidth=0.42)

        self.entrada_cpf_cnpj = Entry(self.menu)
        self.entrada_cpf_cnpj.place(relx=0.27, rely=0.19, relheight=0.03, relwidth=0.20)

        self.entrada_rg = Entry(self.menu)
        self.entrada_rg.place(relx=0.49, rely=0.19, relheight=0.03, relwidth=0.20)


        self.entrada_estado_civil = Entry(self.menu)
        self.entrada_estado_civil.place(relx=0.71, rely=0.19, relheight=0.03, relwidth=0.20)

        self.entrada_data_nascimento = Entry(self.menu)
        self.entrada_data_nascimento.place(relx=0.27, rely=0.26, relheight=0.03, relwidth=0.20)


        self.entrada_sexo = Entry(self.menu)
        self.entrada_sexo.place(relx=0.49, rely=0.26, relheight=0.03, relwidth=0.20)

        self.entrada_profissao = Entry(self.menu)
        self.entrada_profissao.place(relx=0.71, rely=0.26, relheight=0.03, relwidth=0.20)

        self.entrada_endereco = Entry(self.menu)
        self.entrada_endereco.place(relx=0.27, rely=0.33, relheight=0.03, relwidth=0.42)

        self.entrada_numero = Entry(self.menu)
        self.entrada_numero.place(relx=0.71, rely=0.33, relheight=0.03, relwidth=0.20)

        self.entrada_complemento = Entry(self.menu)
        self.entrada_complemento.place(relx=0.27, rely=0.40, relheight=0.03, relwidth=0.31)

        self.entrada_bairro = Entry(self.menu)
        self.entrada_bairro.place(relx=0.61, rely=0.40, relheight=0.03, relwidth=0.30)

        self.entrada_cep = Entry(self.menu)
        self.entrada_cep.place(relx=0.09, rely=0.47, relheight=0.03, relwidth=0.25)

        self.entrada_uf = Entry(self.menu)
        self.entrada_uf.place(relx=0.37, rely=0.47, relheight=0.03, relwidth=0.25)

        self.entrada_cidade = Entry(self.menu)
        self.entrada_cidade.place(relx=0.65, rely=0.47, relheight=0.03, relwidth=0.26)

        self.entrada_telefone = Entry(self.menu)
        self.entrada_telefone.place(relx=0.09, rely=0.54, relheight=0.03, relwidth=0.25)

        self.entrada_celular = Entry(self.menu)
        self.entrada_celular.place(relx=0.37, rely=0.54, relheight=0.03, relwidth=0.25)

        self.entrada_email = Entry(self.menu)
        self.entrada_email.place(relx=0.65, rely=0.54, relheight=0.03, relwidth=0.26)

        self.entrada_observacao = Entry(self.menu)
        self.entrada_observacao.place(relx=0.09, rely=0.62, relheight=0.10, relwidth=0.82)

    # Criação dos botões.
    def botoes(self):
        self.select_image = Button(self.menu, text='Carregar Foto')
        self.select_image.place(relx=0.09, rely=0.33, relheight=0.04, relwidth=0.15)

        self.botao_limpar = Button(self.menu, text='Limpar')
        self.botao_limpar.place(relx=0.09, rely=0.39, relheight=0.04, relwidth=0.15)

        self.botao_cadastrar = Button(self.menu, text='Cadastrar')
        self.botao_cadastrar.place(relx=0.15, rely=0.77, relheight=0.07, relwidth=0.15)

        self.botao_cadastrar = Button(self.menu, text='Banco de Dados')
        self.botao_cadastrar.place(relx=0.42, rely=0.77, relheight=0.07, relwidth=0.15)

        self.botao_cadastrar = Button(self.menu, text='Pesquisar e Alterar')
        self.botao_cadastrar.place(relx=0.70, rely=0.77, relheight=0.07, relwidth=0.15)


menu_cadastro()