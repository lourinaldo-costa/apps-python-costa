# Aula 92
"""
O programa lida com a tentativa do usuário
de tentar logar verificando se o usuário
se encontra no database e se sua senha está
correta e devolve uma mensagem adequada
"""
#Importamos o módulo do tkinter
from tkinter import *

AZUL = '#3784BA'

#importamos o shelve para lidar com o database
import shelve

class Entrada(object):
    def __init__(self, i):
        self.font = ('Verdana', '30', 'bold')

        self.novo = PhotoImage(file = 'Imagens/b_novo.ppm')
        self.cria = PhotoImage(file = 'Imagens/b_criar.ppm')

        imagens = PhotoImage(file = 'Imagens/bg_python.gif') # Não tem o self porque atua como se fosse uma constante

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

        #Depois criamos o título
        self.titulo = Label(self.frame1)
        self.titulo.image = imagens
        self.titulo['image'] = imagens
      
        #Depois criamos o label do usuário
        self.u_l = Label(self.frame1, text = "Usuário", font = self.font, bg = AZUL)
        
        #Colocamos a entry do campo usuário
        self.u_e = Entry(self.frame1, font = self.font)

        #Colocamos a label da senha
        self.s_l = Label(self.frame1, text = "Senha", font = self.font, bg = AZUL)

        #E a entry da senha
        self.s_e = Entry(self.frame1, show = '*', font = self.font)

        #Criamos o botão de entrar
        entrar = PhotoImage(file = 'Imagens/b_entrar.ppm')
        self.e = Button(self.frame2, text = 'Entrar', command = self.Entra)
        self.e['image'] = entrar
        self.e.image = entrar

        #E o botão de novo usuário
        self.n = Button(self.frame2, text = "Novo", command = self.Novo)
        self.n['image'] = self.novo

        #E a label que vai devolver uma msg para o usuário
        self.m_l = Label(self.frame3, text = "")

        #Criamos o botão de deletar
        self.d = Button(self.frame4, text = 'Deleta o cadastro', command = self.Del, font =('Verdana', '15', 'bold') )
        self.d['fg']='red'

        #Criamos o botão 'Lista de cadastrados'
        self.c = Button(self.frame4, text = 'Lista cadastrados', command = self.Cadastrados, font =('Verdana', '15', 'bold') )
        self.c['fg']='blue'

        #Empacotamos os widgets
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.titulo.pack()
        self.u_l.pack()
        self.u_e.pack()
        self.s_l.pack()
        self.s_e.pack()
        self.e.pack(side = LEFT)
        self.n.pack(side = RIGHT)
        self.m_l.pack()
        self.d.pack(side = LEFT)
        self.c.pack(side = RIGHT)
        
        #Abrimos os databases com as senhas
        self.db = shelve.open("login.db")

        #E criamos a variável booleana identificando se estamos no modo criar ou não
        self.criar = False

    def MSG(self, msg, cor = 'red'):
        self.m_l["text"] = msg
        self.m_l["fg"] = cor
        self.m_l["font"] = ('Verdana', '15', 'bold')
    
    def Del(self):
        del self.db[self.u_e.get()]

    def Cadastrados(self):
        with shelve.open("login.db") as arq:
            items = list(arq.items())
            print(items)  

    def Entra(self):
        """
        Função lida com a tentativa do usuário
        de tentar logar verificando se o usuário
        se encontra no database e se sua senha está
        correta e devolve uma mensagem adequada
        """
        usuario = self.u_e.get()
        senha = self.s_e.get()

        if usuario not in self.db:
            self.MSG("Usuário Inválido")
        else:
            if senha == self.db[usuario]:
                self.MSG("Bem vindo %s"%usuario, cor = "blue")
            else:
                self.MSG("Senha Inválida")
    
    def Novo(self):
        """
        Faz as modificações necessárias para entrar no modo
        criar novo usuário e senha
        """
        if not self.criar:
            self.n['image'] = self.cria
            self.u_l['text'] = 'Nome de Usuário'
            self.u_l['fg'] = 'green'
            self.s_l['fg'] = 'green'
            self.criar = True
        else:
            self.Cria()
    
    def Cria(self):
        """
        Método usado para criar um novo usuário
        e uma senha
        """
        usuario = self.u_e.get()
        senha = self.s_e.get()

        if len(senha) == 0 or len(usuario) == 0:
            self.MSG("Nenhum dos campos pode estar vazio!")
        elif usuario in self.db:
            self.MSG("Usuário já existe!")
        else:
            self.db[usuario] = senha
            self.n['image'] = self.novo
            self.u_l['text'] = 'Usuário'
            self.u_l['fg'] = 'black'
            self.s_l['fg'] = 'black'
            self.MSG('Usuário criado com sucesso', 'blue')
            self.criar = False
        


#Inicializamos a nossa janela
i = Tk()

#Inicializamos as variáveis do nosso programa
e = Entrada(i)

#Colocamos um titulo nela
i.title("Login")

#Definimos sua geometria
i.geometry = ("1000x800")

#Definimos uma cor de fundo
i['background'] = AZUL

i.mainloop()





