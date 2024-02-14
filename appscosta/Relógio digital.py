
# Relódio digital

#https://www.geeksforgeeks.org/python-strftime-function/

from tkinter import *
from time import strftime as time

i = Tk()

rel = Label(i, text=time("%H:%M:%S"),font ="Melvetica 120 bold")
rel.pack()

def tictac():
    agora = time("%H:%M:%S")
    if rel['text']!= agora:
        rel['text']= agora
        
    rel.after(100,tictac)

tictac()
i.mainloop()

