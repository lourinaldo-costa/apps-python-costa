# --------------- A classe Tkinter ----------------

from tkinter import*

"""
class Janela:
    def __init__(self, instancia_de_Tk):
        pass

raiz = Tk()
Janela(raiz)
raiz.mainloop
"""
# --------------- O conteiner Frame()  o widget botão ----------------
"""

# O frame tem o tamanho padrão de janela
# O frame tem o tamanho padrão de janela. Quando adiciona frame, a janela passa a ter o tamnho do frame.
# Os frames são elásticos. Seu tamanho é exatamente o tamanhos dos widgets que eles contém.
"""
# --------------- A classe Janela botao1, botao2 e botao3 ----------------
"""

class Janela:
    def __init__(self, toplevel):
        self.fr1 = Frame(toplevel)
        self.fr1.pack()

        self.botao3 = Button(self.fr1)
        self.botao3['text'] = 'Olá!'
        self.botao3['bg'] = 'green'
        self.botao3['fg'] = 'yellow'
        self.botao3['width'] = 12
        self.botao3.pack()

        self.botao1 = Button(self.fr1)
        self.botao1['text'] = 'Costa'
        self.botao1['height']= 5

        self.botao1['bg'] = 'blue'
        self.botao1['fg'] = 'white'
        self.botao1.pack()

        self.botao2 = Button(self.fr1)
        self.botao2['text'] = 'Beleza'
        self.botao2['bg'] = 'yellow'
        self.botao2['fg'] = 'green'
        self.botao2['width'] = 12
        self.botao2.pack()

raiz = Tk()
Janela(raiz)
raiz.mainloop
"""

# --------------- Posicionamento dos widgets ----------------

"""
class Packing:
    
    def __init__(self,instancia_Tk):
        self.container1=Frame(instancia_Tk)
        self.container2=Frame(instancia_Tk)
        self.container3=Frame(instancia_Tk)
        self.container1.pack()
        self.container2.pack()
        self.container3.pack()
        
        self.b1=Button(self.container1,text='B1')
        self.b1.pack()
        
        self.b2=Button(self.container2,text='B2')
        self.b3=Button(self.container2,text='B3')
        self.b2.pack(side=LEFT)
        self.b3.pack(side=LEFT)
  
        self.b4=Button(self.container3,text='B4')
        self.b5=Button(self.container3,text='B5')
        self.b6=Button(self.container3,text='B6')
        self.b6.pack(side=RIGHT)
        self.b5.pack(side=RIGHT)
        self.b4.pack(side=RIGHT)

raiz = Tk()
Packing(raiz)
raiz.mainloop
"""

# --------------- Eventos do mouse ----------------
"""
class Janela:
    
    def __init__(self,toplevel):
        self.frame = Frame(toplevel)
        self.frame.pack()
        self.texto = Label(self.frame, text='Clique para ficar amarelo')
        self.texto['width']=26
        self.texto['height']=3
        self.texto.pack()
        self.botaoverde = Button(self.frame,text='Clique')
        self.botaoverde['background']='green'
        self.botaoverde.bind("<Button-1>",self.muda_cor)  # "<Button-1>" ---> clicar
        self.botaoverde.pack()

    def muda_cor(self, event):
    # Muda a cor do botao!
        if self.botaoverde['bg']=='green':
            self.botaoverde['bg']='yellow'
            self.texto['text']='Clique para ficar verde'
        else:
            self.botaoverde['bg']='green'
            self.texto['text']='Clique para ficar amarelo'

raiz=Tk()
Janela(raiz)
raiz.mainloop()
"""

# --------------- Foco e eventos de teclado ----------------

"""
class Janela:
    
    def __init__(self,toplevel):
        self.frame = Frame(toplevel)
        self.frame.pack()
        self.frame2 = Frame(toplevel)
        self.frame2.pack()
        self.titulo = Label(self.frame,text='VIDENTE 2005', font=('Verdana','16','bold'))
        self.titulo.pack()
        self.msg = Label(self.frame,width=40,height=6, text = 'Adivinho o evento ocorrido!',font=('Verdana','13','bold'))
        self.msg.focus_force()
        self.msg.pack()

       # Definindo o botão 1
        self.b01 = Button(self.frame2,text='Botão 1', font=('Verdana','16','bold'))
        self.b01['padx'],self.b01['pady'] = 10, 5
        self.b01['bg'] = 'deepskyblue'
        self.b01.bind("<Return>",self.keypress01)
        self.b01.bind("<Any-Button>",self.button01)
        self.b01.bind("<FocusIn>",self.fin01)
        self.b01.bind("<FocusOut>",self.fout01)
        self.b01['relief']=RIDGE
        self.b01.pack(side=LEFT)    

# Definindo o botão 2
        self.b02=Button(self.frame2,text='Botão 2',font=('Verdana','16','bold'))
        self.b02['padx'],self.b02['pady'] = 10, 5
        self.b02['bg']='deepskyblue'
        self.b02.bind("<Return>",self.keypress02)
        self.b02.bind("<Any-Button>",self.button02)
        self.b02.bind("<FocusIn>",self.fin02)
        self.b02.bind("<FocusOut>",self.fout02)
        self.b02['relief']=RIDGE  #'relief' muda o relevo do texto 
        self.b02.pack(side=LEFT)
 
    def keypress01(self,event):
        self.msg['text']='ENTER sobre o Botão 1'
    def keypress02(self,event):
        self.msg['text']='ENTER sobre o Botão 2'
    def button01(self,event):
        self.msg['text']='Clique sobre o Botão 1'
    def button02(self,event):
        self.msg['text']='Clique sobre o Botão 2'
    def fin01(self,event):
        self.b01['relief']=FLAT
    def fout01(self,event):
        self.b01['relief']=RIDGE
    def fin02(self,event):
        self.b02['relief']=FLAT
    def fout02(self,event):
        self.b02['relief']=RIDGE

raiz=Tk()
Janela(raiz)
raiz.mainloop()
"""

# --------------- Command binding ----------------

"""
class Janela:
    
    def __init__(self,toplevel):
        self.frame=Frame(toplevel)
        self.frame.pack()

        self.b1=Button(self.frame)
        self.b1.bind("<Button-1>", self.press_b1)  # "<Button-1>" é o evento e 'self.press_b1' é o event handler
        self.b1.bind("<ButtonRelease>", self.release_b1)
        self.b1['text'] = 'Clique em mim!'
        self.b1['width'], self.b1['bg'] = 20, 'brown'
        self.b1['fg']='yellow'
        self.b1.pack(side=LEFT)

        self.b2=Button(self.frame)
        self.b2['width'], self.b2['bg'] = 20, 'brown'
        self.b2['fg']='yellow'
        self.b2.pack(side=LEFT)

        self.b3=Button(self.frame, command = self.click_b3)
        self.b3['width'], self.b3['bg'] = 20, 'brown'
        self.b3['fg']='yellow'
        self.b3.pack(side=LEFT)

    def press_b1(self,event):
        self.b1['text']=''
        self.b2['text']='Errou! Estou aqui!'

    def release_b1(self,event):
        self.b2['text']=''
        self.b3['text']='OOOpa! Mudei de novo!'

    def click_b3(self):  #'click_b3(self)' é o event handler
        self.b3['text']='Ok... Você me pegou...'


instancia=Tk()
Janela(instancia)

instancia.mainloop()
"""

# --------------- O widget Entry ----------------

"""

class Passwords:
    
    def __init__(self,toplevel):
        self.frame1 = Frame(toplevel)
        self.frame1.pack()
        self.frame2 = Frame(toplevel)
        self.frame2.pack()
        self.frame3 = Frame(toplevel)
        self.frame3.pack()
        self.frame4 = Frame(toplevel,pady = 10)
        self.frame4.pack()

        Label(self.frame1,text = 'PASSWORDS', fg ='darkblue', font = ('Verdana','14','bold'), height = 3).pack()
        # Obs1 - Notar que o conteúdo desta Label é constante por isso não tem o self

        fonte1 = ('Verdana','10','bold')

        Label(self.frame2,text = 'Nome: ', font = fonte1,width=8).pack(side=LEFT) # Obs1 
        self.nome = Entry(self.frame2, width=10, font = fonte1)
        self.nome.focus_force() # Para o foco começar neste campo Aqui o cursor fica piscando.
        self.nome.pack(side = LEFT)

        Label(self.frame3,text = 'Senha: ', font = fonte1,width = 8).pack(side = LEFT) # Obs1
        self.senha = Entry(self.frame3, width = 10, show = '*', font = fonte1)
        self.senha.pack(side = LEFT)

        self.confere = Button(self.frame4, font = fonte1, text ='Conferir', bg ='pink', command = self.conferir)
        self.confere.pack()
        self.msg = Label(self.frame4, font = fonte1, height = 3,text = 'AGUARDANDO...')
        self.msg.pack()

    def conferir(self):
        NOME = self.nome.get()
        SENHA = self.senha.get()
        if NOME == SENHA:
            self.msg['text']='ACESSO PERMITIDO'
            self.msg['fg']='darkgreen'
        else:
            self.msg['text']='ACESSO NEGADO'
            self.msg['fg']='red'
            self.nome.focus_force() # Note que o cursor volta pra Entry do nome sugerindo correção.

instancia = Tk()
Passwords(instancia)
instancia.mainloop()
"""

# --------------- Canvas ----------------
"""
class Kanvas:
    
    def __init__(self,raiz):
        self.canvas1 = Canvas(raiz, width=100, height=200, cursor = 'X_cursor', bd = 5, bg ='dodgerblue')
        self.canvas1.pack(side = LEFT)

        self.canvas2 = Canvas(raiz, width = 100, height = 200, cursor = 'dot', bd = 5, bg ='purple')
        self.canvas2.pack(side=LEFT)

# bd = espessura da borda em pixels
# Notar que os canvas estão diretos na janela top-level sem necessidade de frames
# Note que eu preciso empacotar os canvas

instancia = Tk()
Kanvas(instancia)
instancia.mainloop()
"""
# --------------- Canvas - Criando linhas----------------
"""
class Linhas:
    def __init__(self,raiz):
        self.canvas = Canvas(raiz, width = 400, height = 400, cursor ='watch', bd = 5)
        self.canvas.pack()
        self.frame = Frame(raiz)  # Frame para conter os botões 'Esquerda', 'Para cima', 'Para baixo' e 'Dirita'
        self.frame.pack()
        self.last = [200,200]  # Ponto inicial

        configs = {'fg':'darkblue', 'bg':'ghostwhite', 'relief':GROOVE,'width':11,'font':('Verdana','8','bold')}

        self.b1 = Button(self.frame, configs, text ='Esquerda', command = self.left)
        self.b1.pack(side=LEFT)

        self.b2 = Button(self.frame, configs, text='Para cima', command = self.up)
        self.b2.pack(side=LEFT)

        self.b3 = Button(self.frame, configs, text ='Para baixo', command = self.down)
        self.b3.pack(side=LEFT)

        self.b4 = Button(self.frame, configs, text ='Direita', command = self.right)
        self.b4.pack(side=LEFT)

    def left(self): # Desenha um segmento para a esquerda
        x, y = self.last[0]-10, self.last[1]
        self.canvas.create_line(self.last, x, y, fill='red')
        self.last = [x,y]

    def up(self): # Desenha um segmento para cima
        x, y = self.last[0], self.last[1]-10
        self.canvas.create_line(self.last, x, y, fill='yellow')
        self.last = [x,y]

    def down(self): # Desenha um segmento para baixo
        x, y = self.last[0], self.last[1]+10
        self.canvas.create_line(self.last, x, y, fill='blue')
        self.last = [x,y]

    def right(self): # Desenha um segmento para a direita
        x, y = self.last[0]+10, self.last[1]
        self.canvas.create_line(self.last, x, y, fill='purple')
        self.last=[x,y]

instancia = Tk()
Linhas(instancia)
instancia.mainloop()
"""

# --------------- Canvas - Criando Polígonos, retângulos e textos ----------------
"""
class SPFC:
    def __init__(self,raiz):
        self.canvas = Canvas(raiz, width = 200, height = 200, bg ='dodgerblue')
        self.canvas.pack()

        altura = 200 # Altura do canvas. É uma constante. Por isso não tem self.

        pol = self.canvas.create_polygon    # Atribuimos 'self.canvas.create_polygon' à variável pol para não ter que repetir
        ret = self.canvas.create_rectangle  # Idem ao anterior

        pol(100, altura-10, 10, altura-145, 10, altura-190, 190, altura-190, 190, altura-145, 100, altura-10, fill='white')
        ret(15, altura-150, 185, altura-185, fill='black')

        pol(20, altura-140, 95, altura-140, 95, altura-30, 20, altura-140, fill='red')  # Triãngulo vermeho
        pol(105, altura-30, 105, altura-140, 180, altura-140, 105, altura-30, fill='black')  # Triãngulo preto

        self.canvas.create_text(100, altura-167.5, text ='S P F C', font=('Arial','26','bold'), anchor = CENTER, fill='white')

instancia = Tk()
SPFC(instancia)
instancia.mainloop()
"""

# --------------- Canvas - Criando Elipses e arcos, retângulos e textos ----------------
"""
class Fatias:
    def __init__(self,raiz):
        self.canvas = Canvas(raiz, width = 200, height = 250)
        self.canvas.pack()
        self.frame = Frame(raiz)
        self.frame.pack()
        
        self.altura = 200 # Altura do canvas
        
        self.canvas.create_oval(25, self.altura-25, 175, self.altura-175, fill ='deepskyblue', outline ='darkblue')

        fonte =('Comic Sans MS', '14', 'bold')

        Label(self.frame, text ='Fatia: ', font = fonte, fg='blue').pack(side = LEFT)
       
        self.porcentagem = Entry(self.frame, fg='red', font = fonte, width = 5)
        self.porcentagem.focus_force()
        self.porcentagem.pack(side = LEFT)

        Label(self.frame, text ='%', font = fonte, fg ='blue').pack(side=LEFT)

        self.botao = Button(self.frame, text ='Desenhar', command = self.cortar, font = fonte, fg ='darkblue', bg ='deepskyblue')
        self.botao.pack(side=LEFT)

    def cortar(self):
        arco = self.canvas.create_arc
        fatia = float(self.porcentagem.get())*359.9/100.
        arco(25, self.altura-25, 175, self.altura-175, fill ='yellow', outline ='red', extent = fatia)
        self.porcentagem.focus_force()

instancia = Tk()
Fatias(instancia)
instancia.mainloop()
"""
# --------------- Canvas - Criando o Relógio ----------------

from time import localtime

class Horas:
    def __init__(self,raiz):
        self.canvas = Canvas(raiz, width = 265, height = 100)
        self.canvas.pack()
        self.frame = Frame(raiz)
        self.frame.pack()

        self.altura = 100 # Altura do canvas

        # Desenho do relógio-----------------------------
        pol = self.canvas.create_polygon
        ret = self.canvas.create_rectangle
        self.texto = self.canvas.create_text

        self.fonte =('BankGothic Md BT','18','bold')

        pol(10, self.altura-10, 40, self.altura-90, 225, self.altura-90, 255, self.altura-10, fill ='darkblue') # trapézio maior
        pol(18, self.altura-15, 45, self.altura-85, 220, self.altura-85, 247, self.altura-15, fill ='dodgerblue') # trapézio menor
        ret(45, self.altura-35, 90, self.altura-60, fill='darkblue', outline='') # retângulo da hora outline='' significa borda transparente 
        ret(110, self.altura-35, 155, self.altura-60, fill='darkblue', outline='') # retângulo dos minutos
        ret(175, self.altura-35, 220, self.altura-60, fill='darkblue', outline='')
        self.texto(100, self.altura-50, text=':', font = self.fonte, fill='yellow')
        self.texto(165, self.altura-50, text=':', font = self.fonte, fill='yellow')        # Fim do desenho do relógio-----------------------
        # Fim do desenho do relógio-----------------------


        self.mostrar = Button(self.frame, text ='Que horas são?', command = self.mostra, font =('Comic Sans MS', '11', 'bold'), fg ='darkblue', bg ='deepskyblue')
        self.mostrar.pack(side = LEFT)

    def mostra(self):
        self.canvas.delete('digitos_HORA') # Se eu remover o programa funciona.
        self.canvas.delete('digitos_MIN')
        self.canvas.delete('digitos_SEG')
        HORA = str( localtime()[3])  # Corresponde a hora nos argumentos de time.localtime()
        MINUTO = str( localtime()[4]) # Corresponde a minutos
        SEGUNDO = str( localtime()[5])
        self.texto(67.5, self.altura-50, text = HORA, fill='yellow', font = self.fonte, tag ='digitos_HORA')
        self.texto(132.5, self.altura-50, text = MINUTO, fill='yellow', font = self.fonte, tag ='digitos_MIN')
        self.texto(197.5, self.altura-50, text = SEGUNDO, fill='yellow', font = self.fonte, tag ='digitos_SEG')

 


#IMPORTANTE!
"""
Num canvas com dezenas de objetos, algum pode ter relevância grande demais para ser identificado simplesmente com
um número. Por isso, tambem podemos identificar os objetos por meio de strings chamadas 'tag'. A rigor, 'tag' se
comporta como uma opção de configuração definida no instante em que os widgets são criados. Se você quer criar um
círculo e chama-lo de 'bola1' basta fazer: self.nome_do_canvas.criate_oval(coord., opções, tag = 'bola1')
a 'tag' de um objeto tambem pode ser usada como argumento do método 'delete', alem do ID.
"""

instancia = Tk()
Horas(instancia)
instancia.mainloop()

"""
import time
time.strptime("30 Nov 00", "%d %b %y")   
time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0,tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)
                       0           1           2           3         4      5           6           7            8
"""





















    
