# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from pytube import YouTube
import os 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 480)
        MainWindow.setMinimumSize(QtCore.QSize(720, 480))
        MainWindow.setMaximumSize(QtCore.QSize(720, 480))
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.msgBox = QtWidgets.QMessageBox()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 240, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(106, 166, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 240, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(106, 166, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 80, 591, 61))
        self.label.setStyleSheet("font: 75 36pt \"MS Shell Dlg 2\";\n"
"")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 200, 681, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(106, 166, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 200, 31, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.ana) 
        self.pushButton_2.clicked.connect(self.cik) 
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube Downloader"))
        self.pushButton.setText(_translate("MainWindow", "İNDİR"))
        self.pushButton_2.setText(_translate("MainWindow", "ÇIK"))
        self.label.setText(_translate("MainWindow", "YouTube Video Downloader"))
        self.label_2.setText(_translate("MainWindow", " URL"))
    def cik(self):
        exit()
    def msj(self,a):
        self.msgBox.setText(a)
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setWindowTitle("YT Downloader")
        self.msgBox.setStandardButtons(QMessageBox.Ok)
        returnValue = self.msgBox.exec()
    def ana(self):
        if self.lineEdit.text() == "":
            self.msj("Boş Link")
        else:
            try:
                self.link = YouTube(self.lineEdit.text())
                stream=self.link.streams.filter(mime_type="video/mp4" , progressive=True, file_extension='mp4').first().download(filename=self.link.title + ".mp4")
                path =  "./" + self.link.title + ".mp4"
                if os.path.isfile(path) and os.access(path, os.R_OK):
                    self.msj("Dosya İndirildi")
                else:
                    self.msj("Dosya İndirilmedi")
            except:
                self.msj("HATA ! Lütfen Geçerli Bir Link Giriniz")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
