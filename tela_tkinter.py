from tkinter import *
class Janela:
    def __init__(self,toplevel):
        self.fr1 = Frame(toplevel)
        self.fr1.pack()
        self.botao1 = Button(self.fr1,text='Oi!')
        self.botao1['background']='green'
        self.botao1['font']=('Verdana','12','italic','bold')
        self.botao1['height']=3
        self.botao1.pack()
        self.botao2 = Button(self.fr1,bg='red', font=('Times','16'))
        self.botao2['text']='Tchau!'
        self.botao2['fg']='yellow'
        self.botao2['width']=12
        self.botao2.pack()
        self.botao2.pack()
        self.botao3 = Button(self.fr1,bg='red', font=('Times','20'))
        self.botao3['text']='Tchau!'
        self.botao3['fg']='green'
        self.botao3['width']=20
        self.botao3.pack()




#        self.botao = Button(self.fr1, text='Oi Estou testando !', background='green')
#        self.botao.pack()

raiz = Tk()
Janela(raiz)
raiz.mainloop()        