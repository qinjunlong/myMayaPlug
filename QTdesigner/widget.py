import os
from maya import cmds
from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
import importlib

from MyPlug.TestFunction import Classtest_02
from MyPlug.Function_01 import ExportCamer_C
importlib.reload(Classtest_02)
importlib.reload(ExportCamer_C)

CURRENT_FILE = os.path.normpath(__file__)
path, ext = os.path.splitext(CURRENT_FILE)
UI_FILE = path + ".ui"

class TRSConnectorWindow(MayaQWidgetBaseMixin, QtWidgets.QMainWindow):
    def __init__(self,*args, **kwargs):
        super(TRSConnectorWindow, self).__init__(*args, **kwargs)

        self.widget = QUiLoader().load(UI_FILE)
        self.setCentralWidget(self.widget)
        self.setWindowTitle(self.widget.windowTitle())

        self.widget.Pbutton_A.clicked.connect(self.click_A)
        self.widget.Pbutton_B.clicked.connect(self.click_B)
        self.widget.Pbutton_C.clicked.connect(self.click_C)
        


    def click_A(self):

        a = self.widget.Time
        print(a.value())

    def click_B(self):
        clt_B = Classtest_02.test_02()
        clt_B.c2()

    def click_C(self):
        Btime = self.widget.Time.value()
        clt_C = ExportCamer_C.ExportCamer_C(Btime)
        clt_C.CallBTN()
