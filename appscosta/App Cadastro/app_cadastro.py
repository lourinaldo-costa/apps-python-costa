#Importamos o módulo do tkinter
from tkinter import *


AZUL = '#3784BA'

#importamos o shelve para lidar com o database
import shelve


class Entrada(object):
    def __init__(self, i):
        self.mestre = i
        self.font = ('Verdana', '20', 'bold')

        #Frame que contem as entradas de texto
        self.frame1 = Frame(i)
        self.frame1['background'] = AZUL


        #Frame que contem os botões
        self.frame2 = Frame(i)
        self.frame2['background'] = AZUL

        #Frame que contem as mensagens
        self.frame3 = Frame(i)
        self.frame3['background'] = AZUL

        #Frame que contem os botões deleta lista cadastrados
        self.frame4 = Frame(i)
        self.frame4['background'] = 'red'

        self.TelaPrincipal()
        
        #Abrimos os databases com as senhas
        self.bd = shelve.open("cadastro")
        
        #E criamos a variável booleana identificando se estamos no modo criar ou não
        self.criar = False

        #E verificamos se devemos preencher os campos de texto com alguma coisa
        #self.Preenxer()

    def TelaPrincipal(self):
        """
        Cria e impacota os elementos principais do aplicativo
        """
        self.novo = PhotoImage(file = 'Imagens/b_novo.ppm')
        self.cria = PhotoImage(file = 'Imagens/b_criar.ppm')

        imagens = PhotoImage(file = 'Imagens/bg_python.gif')

        #Depois criamos o título
        self.titulo = Label(self.frame1)
        self.titulo.image = imagens
        self.titulo['image'] = imagens
     
        self.Usuario_Senha()

        #Então criamos o checkbutton lembrar
        #self.c_b = Checkbutton(self.frame1, font = self.font, text = 'Lembrar-me', bg = AZUL, command = self.Lembrar)
        #self.selecionado = False
        
        #Criamos o botão de entrar
        #entrar = PhotoImage(file = 'Imagens/b_entrar.ppm')
        self.e = Button(self.frame2, text = 'Entrar', font = self.font, command = self.Entra)
        #self.e['image'] = entrar
        #self.e.image = entrar

        #E o botão de novo usuário
        self.n = Button(self.frame2, text = "Novo",font = self.font, command = self.Novo)
        #self.n['image'] = self.novo

        #Empacotamos os widgets
        self.EmpacotaTelaPrincipal()

        #EmpacotaTelaPrincipal()
    def EmpacotaTelaPrincipal(self):
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.titulo.pack()
        self.u_l.pack()
        self.u_e.pack()
        self.s_l.pack()
        self.s_e.pack()
        #self.c_b.pack()
        self.m_l.pack()
        self.e.pack(side = LEFT)
        self.n.pack(side = RIGHT)
        self.d.pack(side = LEFT)
        self.c.pack(side = RIGHT)

    def Usuario_Senha(self):
        """
        Cria os campos de usuário e senha
        """
        #Depois criamos o label do usuário
        self.u_l = Label(self.frame1, text = "Usuário", font = self.font, bg = AZUL)
        
        #Colocamos a entry do campo usuário
        self.u_e = Entry(self.frame1, font = self.font)

        #Colocamos a label da senha
        self.s_l = Label(self.frame1, text = "Senha", font = self.font, bg = AZUL)

        #E a entry da senha
        self.s_e = Entry(self.frame1, show = '*', font = self.font)

        #E a label que vai devolver uma msg para o usuário
        self.m_l = Label(self.frame3, text = "", font = ('Verdana', '10', 'bold'))

        #Criamos o botão de deletar
        self.d = Button(self.frame4, text = 'Deleta o cadastro', command = self.Del, font =('Verdana', '15', 'bold') )
        self.d['fg']='red'

        #Criamos o botão 'Lista de cadastrados'
        self.c = Button(self.frame4, text = 'Lista cadastrados', command = self.Cadastrados, font =('Verdana', '15', 'bold') )
        self.c['fg']='blue'


    #def Preenxer(self):
        #if 'Lembrar' in self.bd:
            #self.u_e.insert(0, self.bd['Lembrar']['Usuário'])
            #self.s_e.insert(0, self.bd['Lembrar']['Senha'])


    def MSG(self, msg, cor = 'red'):
        self.m_l["text"] = msg
        self.m_l["fg"] = cor

    def Del(self):
        del self.bd[self.u_e.get()]

    def Cadastrados(self):
        with shelve.open("cadastro") as arq:
            items = list(arq.items())
            print(items)  

    #def Lembrar(self):
        """
        Função que troca o estado da variável do checkbutton
        """
        #self.selecionado = not self.selecionado
    
    def Entra(self):
        """
        Função lida com a tentativa do usuário
        de tentar logar verificando se o usuário
        se encontra no database e se sua senha está
        correta e devolve uma mensagem adequada
        """
        usuario = self.u_e.get()
        senha = self.s_e.get()

        if usuario not in self.bd:
            self.MSG("Usuário Inválido")
        else:
            if senha == self.bd[usuario]['Senha']:
                self.MSG("Bem vindo %s"%usuario, cor = "blue")
                
                #if self.selecionado:
                    #self.bd['Lembrar'] = {'Usuário': usuario, 'Senha': senha}
            else:
                self.MSG("Senha Inválida")
    
    def Novo(self):
        """
        Faz as modificações necessárias para entrar no modo
        criar novo usuário e senha
        """
        self.l_nome = Label(self.frame1, text = 'Nome', font = self.font, bg = AZUL)
        self.e_nome = Entry(self.frame1, font = self.font)
        self.l_email = Label(self.frame1, text = 'Email', font = self.font, bg = AZUL)
        self.e_email = Entry(self.frame1, font = self.font)
        self.b_criar = Button(self.frame1, text = "Criar", font = self.font, command = self.Cria)

        self.EmpacotaCria()
    
    def Cria(self):
        """
        Método usado para criar um novo usuário
        e uma senha
        """
        usuario = self.u_e.get()
        senha = self.s_e.get()
        nome = self.e_nome.get()
        email = self.e_email.get()

        if len(senha) == 0 or len(usuario) == 0 or len(nome) == 0 or len(email) == 0:
            self.MSG("Nenhum dos campos pode estar vazio!")
        elif usuario in self.bd:
            self.MSG("Usuário já existe!")
        else:
            self.bd[usuario] = {'Nome': nome, 'Email': email, 'Senha': senha}
            self.u_e.delete(0, END)
            self.s_e.delete(0, END)     
            self.MSG('Usuário criado com sucesso', 'blue')
     
        #Empacota Cria
    def EmpacotaCria(self):
        self.l_nome.pack()
        self.e_nome.pack()
        self.l_email.pack()
        self.e_email.pack()
        self.b_criar.pack()
             
        
#Inicializamos a nossa janela
i = Tk()

#Inicializamos as variáveis do nosso programa
e = Entrada(i)

#Colocamos um titulo nela
i.title("Login")

#Definimos sua geometria
i.geometry = ("800x1000")

i.resizable(True, True) # i.resizable(height = None, width = None) ou i.resizable(height = 0, 0)
                          # ou i.resizable(height = False, False)
                          # i.resizable(height = 1, 1) ou i.resizable(height = True, True)

#Definimos uma cor de fundo
i['background'] = AZUL

i.mainloop()

