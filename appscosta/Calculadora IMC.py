# Calculadora de IMC

# https://www.youtube.com/watch?v=CrZkNmpPWVo&t=2593s

# O Índice de massa corporal é um cálculo simples usando a altura e o peso de uma pessoa.

# Rastrear o seu IMC é uma maneira útil de verificar se você está mantendo um peso saudável.
# É calculado usando o peso e a altura de uma pessoa , usando esta fórmula: peso/altura**2

# O número resultante indica uma das seguintes categorias:
"""
Abaixo do peso = menos de 18,5
Normal = maior ou igual a 18,5 e menor do que 25
Sobrepeso = maior ou igual a 25 e menor do que 30
Obesidade = 30 ou mais
"""
# O programa levará o peso e a altura de uma pessoa como entrada e gera a categoria
# de IMC correspondente.


from tkinter import*
from tkinter import ttk

# Cores
co0 = '#ffffff'  #branca/white
co1 = '#444466'  #preta/black
co2 = '#4065a1'  # azul/blue

tela = Tk()
tela.title("Calculadora IMC")
tela.geometry('295x230')
tela.configure(bg = 'yellow')

#----------- Dividindo a tela em duas partes(frame cima e frame baixo) ------------

frame_c = Frame(tela, width = 295, height = 50, bg = co0, pady = 0, padx = 0, relief = 'flat')
frame_c.grid(row=0, column=0, stick=NSEW)
frame_b = Frame(tela, width = 295, height = 180, bg = co0, pady = 0, padx = 0, relief = 'flat')
frame_b.grid(row=1, column=0, stick=NSEW)

#----------- Parte lógica - Cálculos ------------

def calcular():
    peso = float(e_peso.get())
    altura = float(e_altura.get())

    imc = peso/altura**2

    resultado = imc

    if resultado < 18.5:
        l_resultado_texto['text'] = 'Seu IMC indica: abaixo do peso'

    elif resultado >= 18.5 and resultado < 25:
        l_resultado_texto['text'] = 'Seu IMC indica: normal'

    elif resultado >= 25 and resultado < 30:
        l_resultado_texto['text'] = 'Seu IMC indica: sobrepeso'

    else:
        l_resultado_texto['text'] = 'Seu IMC indica: obesidade'
        

    l_resultado['text']  = "{:.{}f}".format(resultado,2) # Substitui o 'text' de 'l_resultado' que está com '---' por "{:.{}f}".format(resultado,2).

    
#----------- Configurando o frame cima ------------

app_nome = Label(frame_c, text='Calculadora de IMC', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 16 bold'), bg=co0, fg=co1)
app_nome.place(x=0, y=0)

app_linha = Label(frame_c, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 1'), bg=co1, fg=co1)
app_linha.place(x=0, y=35)                                                                                                                   

#----------- Configurando o frame baixo ------------

l_peso = Label(frame_b, text='Insira seu peso', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
l_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3) # a width vou manter automático. stick=NSEW para posicionar numa forma melhor
e_peso = Entry(frame_b, width=5, relief='solid',  font=('Ivy 10 bold'), justify = 'center')
e_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3) 

l_altura = Label(frame_b, text='Insira sua altura', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
l_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3) 
e_altura = Entry(frame_b, width=5, relief='solid',  font=('Ivy 10 bold'), justify = 'center')
e_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

l_resultado = Label(frame_b, text='---', width=5, height=1, padx=6, pady=12, relief='flat', anchor='center', font=('Ivy 24 bold'), bg=co2, fg=co0)
l_resultado.place(x=169, y=10)  # Se usar o 'grid' dá muito trabalho e precisa muita paciência tentando acertar. Usando o 'place' é mais simples e tem mais
                                # liberdade para mover para qualquer canto da tela que eu bem entender

                    
l_resultado_texto = Label(frame_b, text='', width=37, height=1, padx=0, pady=12, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
l_resultado_texto.place(x=0, y=85)

b_calcular = Button(frame_b, command = calcular, text='Calcular', width=33, height=1, overrelief=SOLID, relief='raised', anchor='center', font=('Ivy 10 bold'), bg=co2, fg=co0)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=25)



tela.mainloop()











