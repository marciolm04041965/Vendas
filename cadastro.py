from PySimpleGUI import PySimpleGUI as sg

# Layout related
sg.theme("Reddit")
layout = [
    [sg.Text('Usuario:'),sg.Input(key='usuario',size=(20,1))],
    [sg.Text('Senha  :'),sg.Input(key='senha',password_char='*',size=(20,1))],
    [sg.Checkbox("Salvar o Login?")],
    [sg.Button("Entrar")]
]

# Janela
janela = sg.Window('Tela de Login',layout)

# Ler os Eventos
while True:
    eventos,valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == "Entrar":
        if valores['usuario'] == 'marcio' and valores['senha']=="123456" :
            print("Bem vindo a Dev Aprender")

