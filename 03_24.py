import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pyupbit

form_class = uic.loadUiType("mywindow.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inquiry)
    def inquiry(self):
        price = pyupbit.get_current_price("KRW-BTC")
        print("비트코인 현재가")
        self.lineEdit.setText(str(price)) 
        price = pyupbit.get_current_price("KRW-ETH")
        print("이더리움 현재가")
        self.lineEdit_2.setText(str(price)) 

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
