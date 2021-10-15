from tkinter import *
class Janela:
    def __init__(self,toplevel):
        self.frame=Frame(toplevel)
        self.frame.pack()
        self.texto=Label(self.frame, text='Clique para ficar amarelo')
        self.texto['width']=26
        self.texto['height']=3
        self.texto.pack()
        self.botaoverde=Button(self.frame,text='Clique')
        self.botaoverde['background']='green'
        self.botaoverde.bind("<Button-1>",self.muda_cor)
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