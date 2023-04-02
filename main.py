import time
import datetime as dt   
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from sys import argv


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('GUI.ui',self)
        host = "C:\Windows\System32\drivers\etc\hosts"
        temp_host= "C:\Windows\System32\drivers\etc\hosts"




app = QApplication(argv)
window = MainWindow()
window.show()
app.exec_()