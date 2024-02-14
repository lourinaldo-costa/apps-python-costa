print()

# https://acervolima.com/como-definir-a-borda-do-widget-de-etiqueta-do-tkinter/

from tkinter import*
from tkinter import ttk

# Cores
co0 = '#ffffff'  #branca/white
co1 = '#444466'  #preta/black
co2 = '#4065a1'  # azul/blue
co3 = '#C6D1DE'

tela = Tk()
tela.title("")
tela.geometry('355x350')
tela.configure(bg = '#C6D1DE')

#----------- Dividindo a tela em duas partes(frame cima e frame baixo) ------------

frame_c = Frame(tela, width = 295, height = 50, bg = co0, pady = 0, padx = 0, relief = 'flat')
frame_c.grid(row=0, column=0, stick=NSEW)
frame_b = Frame(tela, width = 295, height = 180, bg = co0, pady = 0, padx = 0, relief = 'flat')
frame_b.grid(row=1, column=0, stick=NSEW)

#----------- Parte lógica ------------

def cal_fin():
    v = float(e_valor_vista.get())
    e = float(e_entrada.get())
    n = float(e_meses.get())
    i = float(e_tjm.get())
    j = i/100

    tja = ((j+1)**12-1)
    l_resultado1['text'] = f'{tja:,.2%}' 

    vf = v-e
    texto_vf = f'{vf:_.2f}'
    texto_vf = texto_vf.replace('.',',').replace('_','.')
    l_resultado2['text'] = texto_vf.replace('.',',').replace('_','.') 

    fac = (1+j)**n

    p = vf*fac*j/(fac-1)
    texto_p = f'{p:_.2f}'
    texto_p = texto_p.replace('.',',').replace('_','.')
    l_resultado3['text'] = texto_p.replace('.',',').replace('_','.')

    vtf = n*p
    texto_vtf = f'{vtf:_.2f}'
    texto_vtf = texto_vtf.replace('.',',').replace('_','.')
    l_resultado4['text'] = texto_vtf.replace('.',',').replace('_','.')

    vtc = e+vtf
    texto_vtc = f'{vtc:_.2f}'
    texto_vtc = texto_vtc.replace('.',',').replace('_','.')
    l_resultado5['text'] = texto_vtc.replace('.',',').replace('_','.') 

    jp = vtf-vf
    texto_jp = f'{jp:_.2f}'
    texto_jp = texto_jp.replace('.',',').replace('_','.')
    l_resultado6['text'] = texto_jp.replace('.',',').replace('_','.')

#----------- Configurando o frame cima ------------

app_nome = Label(frame_c, text='Calculadora Financeira', width=23, height=1, padx=5, relief='flat', anchor='center', font=('Ivy 16 bold'), bg=co0, fg='blue')
app_nome.place(x=0, y=0)

app_linha = Label(frame_c, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 1'), bg=co3, fg=co1)
app_linha.place(x=0, y=35)                                                                                                                   

#----------- Configurando o frame baixo ------------

l_parametros = Label(frame_b, text='Parâmetros', width = 22, height=0, padx=0, anchor="w", font=('Ivy 11 bold'), bg=co0, fg=co1)
l_parametros.grid(row=0, column=0, sticky=NSEW, pady=0, padx=0) 
l_unidade = Label(frame_b, text='Unid', width = 5, height=0, padx=0, anchor='center', font=('Ivy 11 bold'), bg=co0, fg=co1)
l_unidade.grid(row=0, column=1, sticky=NSEW, pady=0, padx=3) 
l_valor = Label(frame_b, text='Valor', width = 10, height=0, padx=0, anchor='center', font=('Ivy 11 bold'), bg=co0, fg=co1)
l_valor.grid(row=0, column=2, sticky=NSEW, pady=0, padx=3)

l_valor_vista = Label(frame_b, text='Valor à Vista', width = 22, height=0, padx=0, anchor="w", font=('Ivy 11 bold'), bg=co3, fg=co1)
l_valor_vista.grid(row=1, column=0, sticky=NSEW, pady=0, padx=0) 
l_r_valor_vista = Label(frame_b, text='R$', width = 5, height=0, padx=0, anchor='center', font=('Ivy 11 bold'), bg=co3, fg=co1)
l_r_valor_vista.grid(row=1, column=1, sticky=NSEW, pady=0, padx=3) 
e_valor_vista = Entry(frame_b, width=10,  font=('Ivy 11 bold'), justify = 'center', relief = 'solid', bg = '#FFFF99')
e_valor_vista .grid(row=1, column=2, sticky=NSEW, pady=0, padx=3) 

l_entrada = Label(frame_b, text='Entrada', width = 22, height=0, padx=0, anchor="w", font=('Ivy 11 bold'), bg=co3, fg=co1)
l_entrada.grid(row=2, column=0, sticky=NSEW, pady=0, padx=0) 
l_r_entrada = Label(frame_b, text='R$', width = 5, height=0, padx=0, anchor='center', font=('Ivy 11 bold'), bg=co3, fg=co1)
l_r_entrada.grid(row=2, column=1, sticky=NSEW, pady=0, padx=3) 
e_entrada = Entry(frame_b, width=10, font=('Ivy 11 bold'), justify = 'center', relief = 'solid', bg = '#FFFF99')
e_entrada .grid(row=2, column=2, sticky=NSEW, pady=0, padx=3) 

l_periodos = Label(frame_b, text='Nº de Períodos', width = 22, height=0, padx=0, anchor="w", font=('Ivy 11 bold'), bg=co3, fg=co1)
l_periodos.grid(row=3, column=0, sticky=NSEW, pady=0, padx=0) 
l_meses = Label(frame_b, text='meses', width = 5, height=0, padx=0, anchor='center', font=('Ivy 11 bold'), bg=co3, fg=co1)
l_meses.grid(row=3, column=1, sticky=NSEW, pady=0, padx=3) 
e_meses = Entry(frame_b, width=10,  font=('Ivy 11 bold'), justify = 'center', relief = 'solid',bg = '#FFFF99')
e_meses.grid(row=3, column=2, sticky=NSEW, pady=0, padx=3) 

l_tjm = Label(frame_b, text='Taxa de Juros ao mês', width = 22, height=0, padx=0, anchor="w", font=('Ivy 11 bold'), bg=co3, fg=co1)
l_tjm.grid(row=4, column=0, sticky=NSEW, pady=0, padx=0) 
l_porc_m = Label(frame_b, text='%', width = 5, height=0, padx=0, anchor='center', font=('Ivy 11 bold'), bg=co3, fg=co1)
l_porc_m.grid(row=4, column=1, sticky=NSEW, pady=0, padx=3) 
e_tjm = Entry(frame_b, width=10,  font=('Ivy 11 bold'), justify = 'center', relief = 'solid',bg = '#FFFF99')
e_tjm.grid(row=4, column=2, sticky=NSEW, pady=0, padx=3) 

l_tja = Label(frame_b, text='Taxa de Juros ao ano', width = 22, height=0, padx=0, anchor="w", font=('Ivy 11 bold'), bg=co3, fg=co1)
l_tja.grid(row=5, column=0, sticky=NSEW, pady=0, padx=0) 
l_porc_a = Label(frame_b, text='%', width = 5, height=0, padx=0, anchor='center', font=('Ivy 11 bold'), bg=co3, fg=co1)
l_porc_a.grid(row=5, column=1, sticky=NSEW, pady=0, padx=3) 
l_resultado1 = Label(frame_b, text='---', width = 10, height=0, padx=0, anchor='center', font=('Ivy 11 bold'), bg = '#FFFF99', fg=co1)
l_resultado1.grid(row=5, column=2, sticky=NSEW, pady=0, padx=3)

l_valor_fin = Label(frame_b, text='V-E=Valor Financiado', width = 22, height=0, padx=0, anchor="w", font=('Ivy 11 bold'), bg=co3, fg=co1)
l_valor_fin.grid(row=6, column=0, sticky=NSEW, pady=0, padx=0) 
l_r_fin = Label(frame_b, text='R$', width = 5, height=0, padx=0, anchor='center', font=('Ivy 11 bold'), bg=co3, fg=co1)
l_r_fin.grid(row=6, column=1, sticky=NSEW, pady=0, padx=3) 
l_resultado2 = Label(frame_b, text='---', width = 10, height=0, padx=0, anchor='center', font=('Ivy 11 bold'), bg = '#FFFF99', fg=co1)
l_resultado2.grid(row=6, column=2, sticky=NSEW, pady=0, padx=3)

#----------- Labels resultados ------------

l_valor_prest = Label(frame_b, text='P=Valor da Prestação', width = 22, height=0, padx=0, anchor="w", font=('Ivy 11 bold'), bg='yellow', fg=co1)
l_valor_prest.grid(row=7, column=0, sticky=NSEW, pady=0, padx=0) 
l_r_fin = Label(frame_b, text='R$', width = 5, height=0, padx=0, anchor='center', font=('Ivy 11 bold'), bg='yellow', fg=co1)
l_r_fin.grid(row=7, column=1, sticky=NSEW, pady=0, padx=3) 
l_resultado3 = Label(frame_b, text='---', width = 10, height=0, padx=0, relief = 'flat', anchor='center', font=('Ivy 11 bold'), bg='yellow', fg=co1)
l_resultado3.grid(row=7, column=2, sticky=NSEW, pady=0, padx=3)

l_valor_tot_fin = Label(frame_b, text='VTF=Valor Total Financiado', width = 22, height=0, padx=0, anchor="w", font=('Ivy 11 bold'), bg=co3, fg=co1)
l_valor_tot_fin.grid(row=8, column=0, sticky=NSEW, pady=0, padx=0) 
l_r_valor_tot_fin = Label(frame_b, text='R$', width = 5, height=0, padx=0, anchor='center', font=('Ivy 11 bold'), bg=co3, fg=co1)
l_r_valor_tot_fin.grid(row=8, column=1, sticky=NSEW, pady=0, padx=3) 
l_resultado4 = Label(frame_b, text='---', width = 10, height=0, padx=0, anchor='center', font=('Ivy 11 bold'), bg='#FFFF99', fg=co1)
l_resultado4.grid(row=8, column=2, sticky=NSEW, pady=0, padx=3)

l_valor_tot_compra = Label(frame_b, text='VTC=Valor Total da Compra', width = 22, height=0, padx=0, anchor="w", font=('Ivy 11 bold'), bg=co3, fg=co1)
l_valor_tot_compra.grid(row=9, column=0, sticky=NSEW, pady=0, padx=0) 
l_r_valor_tot_compra = Label(frame_b, text='R$', width = 5, height=0, padx=0, anchor='center', font=('Ivy 11 bold'), bg=co3, fg=co1)
l_r_valor_tot_compra.grid(row=9, column=1, sticky=NSEW, pady=0, padx=3) 
l_resultado5 = Label(frame_b, text='---', width = 10, height=0, padx=0, anchor='center', font=('Ivy 11 bold'), bg='#FFFF99', fg=co1)
l_resultado5.grid(row=9, column=2, sticky=NSEW, pady=0, padx=3)

l_juros_pagos = Label(frame_b, text='Juros Pagos', width = 22, height=0, padx=0, anchor="w", font=('Ivy 11 bold'), bg=co3, fg=co1)
l_juros_pagos.grid(row=10, column=0, sticky=NSEW, pady=0, padx=0) 
l_r_juros_pagos = Label(frame_b, text='R$', width = 5, height=0, padx=0, anchor='center', font=('Ivy 11 bold'), bg=co3, fg=co1)
l_r_juros_pagos.grid(row=10, column=1, sticky=NSEW, pady=0, padx=3) 
l_resultado6 = Label(frame_b, text='---', width = 10, height=0, padx=0, anchor='center', font=('Ivy 11 bold'), bg='#FFFF99', fg=co1)
l_resultado6.grid(row=10, column=2, sticky=NSEW, pady=0, padx=3)

b_calcular = Button(frame_b, text='Calcular', command = cal_fin, width=15, height=1, overrelief=SOLID, relief='raised', anchor='center', font=('Ivy 12 bold'), bg=co3, fg='blue')
b_calcular.grid(row=11, column=0, sticky=NSEW, pady=0, padx=0, columnspan=1)


def clear():
        e_valor_vista.delete(0,END)
        e_entrada.delete(0,END)
        e_meses.delete(0,END)
        e_tjm.delete(0,END)
        

b_delete = Button(frame_b, text='Limpa', width=15, height=1, overrelief=SOLID, relief='raised', anchor='center',
                  font=('Ivy 12 bold'), bg=co3, fg='blue', command = clear)
b_delete.grid(row=11, column=1, sticky=NSEW, pady=0, padx=0, columnspan=3)

tela.mainloop()

"""

from tkinter import *
window = Tk() 
window.title('GFG') 
A = Label(window, text="flat", width=10, 
          height=2, borderwidth=3, relief="flat") 
B = Label(window, text="solid", width=10, 
          height=2, borderwidth=3, relief="solid") 
C = Label(window, text="raised", width=10, 
          height=2, borderwidth=3, relief="raised") 
D = Label(window, text="sunken", width=10, 
          height=2, borderwidth=3, relief="sunken") 
E = Label(window, text="ridge", width=10, 
          height=2, borderwidth=3, relief="ridge") 
F = Label(window, text="groove", width=10, 
          height=2, borderwidth=3, relief="groove") 
A.grid(column=0, row=1, padx=100, pady=10) 
B.grid(column=0, row=2, padx=100, pady=10) 
C.grid(column=0, row=3, padx=100, pady=10) 
D.grid(column=0, row=4, padx=100, pady=10) 
E.grid(column=0, row=5, padx=100, pady=10) 
F.grid(column=0, row=6, padx=100, pady=10) 
  
window.mainloop() 

"""









































