import time
from datetime import datetime as dt   
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from sys import argv

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('GUI.ui',self)
        self.Handel_buttons()
        self.redirect="127.0.0.1"
        self.host="C:\Windows\System32\drivers\etc\hosts"
        self.websites = []
    def Handel_buttons(self):
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.start)
    def add(self):
        self.blockedWebsite= 'www.' + (self.lineEdit.text())
        self.websites.append(self.blockedWebsite)
        self.lineEdit.clear()
        print(self.websites)
    def start(self):
            self.FROM=self.timeEdit.text()
            self.From_std=int(self.FROM[0:2])
            self.From_min=int(self.FROM[3:])
            self.TO=self.timeEdit_2.text()
            self.To_std=int(self.TO[0:2])
            self.To_min=int(self.TO[3:])
            if dt(dt.now().year,dt.now().month,dt.now().day,self.From_std,self.From_min)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,self.To_std,self.To_min):
                with open(self.host,'r+') as self.file:
                    self.content=self.file.readlines()
                    for self.website in self.websites:
                        if (f'{self.redirect} {self.website} \n') in self.content:
                            print('there is a website')
                            pass
                        else:
                            self.content.insert(20,f'{self.redirect} {self.website} \n')
                            self.file.seek(0)
                            self.file.writelines(self.content)
            else:
                with open(self.host,'r+') as self.file:
                    self.content=self.file.readlines()
                    for self.website in self.websites:
                        if (f'{self.redirect} {self.website} \n') in self.content:
                            self.content.remove(f'{self.redirect} {self.website} \n')
                            self.file.seek(0)
                            self.file.writelines(self.content)



app = QApplication(argv)
window = MainWindow()
window.show()
app.exec_()