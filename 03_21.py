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
        print("현재 비트코인의 가격은", price, "입니다.")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
