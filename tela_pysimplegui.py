import PySimpleGUI as sg


class TelaPython:
    def __init__(self):
        #sg.change_look_and_feel("TanBlue")
        # layout 
        layout = [
            [sg.Text("Nome",size=(5,0),font="Courier 12",text_color="blue",background_color='green'),sg.Input(size=(15,0),key="nome")],
            [sg.Text("Idade",size=(5,0)),sg.Input(size=(15,0),key="idade")],
            [sg.Text("Quais provedores e E-mail são aceitos?")],
            [sg.Checkbox('Gmail',key="gmail"),sg.Checkbox('Yahoo',key="yahoo"),sg.Checkbox("Outlook",key="outlook")],
            [sg.Text("Aceita cartão")],
            [sg.Radio("Sim","Cartoes",key="sim_aceita"),sg.Radio("Não","Cartoes",key="nao_aceita")],
            [sg.Slider(range=(0,255),orientation="h",size=(15,20),key="sliderVelocidade",default_value=0)],
            [sg.OK(),sg.Cancel()],
            [sg.Button("Enviar Dados")],
            [sg.Output(size=(30,20))],
        ]

        # janela
        self.janela = sg.Window("Dados do Usuario").layout(layout)
        # Extrair os dados da tela python
        #self.button, self.values = self.janela.read()

    def Iniciar(self):

        while True:
            self.button, self.values = self.janela.read()
            if self.button in (sg.WIN_CLOSED,"Cancel"):
                windows.close()

            nome = self.values["nome"]
            idade= self.values["idade"]
            aceita_gmail   = self.values["gmail"]
            aceita_yahoo   = self.values["yahoo"]
            aceita_outlook = self.values["outlook"]
            sim_aceita_cartao  = self.values["sim_aceita"]
            nao_aceita_cartao  = self.values["nao_aceita"]
            sliderVelocidade = self.values["sliderVelocidade"]

            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Aceita Gmail: {aceita_gmail}')
            print(f'Aceita Yahoo: {aceita_yahoo}')
            print(f'Aceita OutLook: {aceita_outlook}')
            print(f'Aceita cartão :{sim_aceita_cartao}')
            print(f'Não Aceita cartão :{nao_aceita_cartao}')
            print(f'velocidde : {sliderVelocidade}')

tela = TelaPython()
tela.Iniciar()           

