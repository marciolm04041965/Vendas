# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'radio_box.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_TeladeRadionBOX(object):
    def setupUi(self, TeladeRadionBOX):
        if not TeladeRadionBOX.objectName():
            TeladeRadionBOX.setObjectName(u"TeladeRadionBOX")
        TeladeRadionBOX.resize(800, 600)
        TeladeRadionBOX.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.centralwidget = QWidget(TeladeRadionBOX)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 65, 221, 61))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"")
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(310, 160, 95, 20))
        font1 = QFont()
        font1.setFamilies([u"Bell MT"])
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(True)
        self.radioButton.setFont(font1)
        self.radioButton.setStyleSheet(u"selection-background-color: rgb(0, 0, 255);")
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(310, 230, 95, 20))
        font2 = QFont()
        font2.setFamilies([u"Bell MT"])
        font2.setPointSize(14)
        font2.setItalic(True)
        self.radioButton_2.setFont(font2)
        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(310, 300, 95, 20))
        self.radioButton_3.setFont(font2)
        self.radioButton_4 = QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(310, 380, 95, 20))
        self.radioButton_4.setFont(font2)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 450, 121, 61))
        self.pushButton.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        self.resposta = QLabel(self.centralwidget)
        self.resposta.setObjectName(u"resposta")
        self.resposta.setGeometry(QRect(190, 520, 391, 41))
        font3 = QFont()
        font3.setPointSize(28)
        font3.setBold(True)
        self.resposta.setFont(font3)
        TeladeRadionBOX.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TeladeRadionBOX)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        TeladeRadionBOX.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TeladeRadionBOX)
        self.statusbar.setObjectName(u"statusbar")
        TeladeRadionBOX.setStatusBar(self.statusbar)

        self.retranslateUi(TeladeRadionBOX)

        QMetaObject.connectSlotsByName(TeladeRadionBOX)
    # setupUi

    def retranslateUi(self, TeladeRadionBOX):
        TeladeRadionBOX.setWindowTitle(QCoreApplication.translate("TeladeRadionBOX", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("TeladeRadionBOX", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Selecione Uma Cor</span></p></body></html>", None))
        self.radioButton.setText(QCoreApplication.translate("TeladeRadionBOX", u"Azul", None))
        self.radioButton_2.setText(QCoreApplication.translate("TeladeRadionBOX", u"Vermelho", None))
        self.radioButton_3.setText(QCoreApplication.translate("TeladeRadionBOX", u"Amarelo", None))
        self.radioButton_4.setText(QCoreApplication.translate("TeladeRadionBOX", u"Branco", None))
        self.pushButton.setText(QCoreApplication.translate("TeladeRadionBOX", u"Enviar", None))
        self.resposta.setText("")
    # retranslateUi

