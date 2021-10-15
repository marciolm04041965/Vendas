from PyQt6 import QtWidgets,uic
import sys

def funcao_principal():
    if formulario.radioButton.isChecked():
        opcao = "Opcao 1 Selecionada"
     
    elif formulario.radioButton_2.isChecked():
        opcao = "Opcao 2 Selecionada"
        
    elif formulario.radioButton_3.isChecked():
        opcao = "Opcao 3 Selecionada"
        
    elif formulario.radioButton_4.isChecked():
        opcao = "Opcao 4 Selecionada"
        
    else:
        print("não Selecionada") 

    formulario.resposta.setText(opcao) 

app = QtWidgets.QApplication([])
formulario = uic.loadUi("radio_box.ui")
formulario.pushButton.clicked.connect(funcao_principal)


formulario.show()
app.exec()






