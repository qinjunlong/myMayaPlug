from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from MyPlug.TestFunction import Classtest_02
from MyPlug.Function_01 import ExportCamer_C
import importlib

importlib.reload(Classtest_02)
importlib.reload(ExportCamer_C)


class win(QWidget):
    def __init__(self):
        super(win,self).__init__()
        self.setWindowTitle("Flame")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.button_01 = QPushButton("click")
        self.button_02 = QPushButton("click")
        self.button_03 = QPushButton("click")
        self.layout.addWidget(self.button_01)
        self.layout.addWidget(self.button_02)
        self.layout.addWidget(self.button_03)
        self.button_01.clicked.connect(self.printHelloWorld)
        self.button_02.clicked.connect(self.clt)
        self.button_03.clicked.connect(self.Pbutton_03)
        self.show()

    def printHelloWorld(self):
        print("button_01")

    def clt(self):
        clt_Ins = Classtest_02.test_02()
        clt_Ins.c2()

    def Pbutton_03(self):
        Pbutton_03_Ins = ExportCamer_C.ExportCamer_C()
        Pbutton_03_Ins.CallBTN()


a = win()
