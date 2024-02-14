
from time import strftime as time
rel = tk.Label(text=time("%H:%M:%S"),font ="Melvetica 120 bold")
rel.pack()

def tictac():
    agora = time("%H:%M:%S")
    if rel['text']!= agora:
        rel['text']= agora
        
    rel.after(100,tictac)

tictac()
rel.mainloop
