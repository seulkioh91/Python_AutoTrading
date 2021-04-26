import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit

form_class = uic.loadUiType("mywindow.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inquiry)

    def inquiry(self):
        price1 = pykorbit.get_current_price("BTC")
        self.lineEdit_1.setText(str(price1)) 
        print("현재 비트코인의 가격은", price1, "입니다.")
        price2 = pykorbit.get_current_price("ETH")
        self.lineEdit_2.setText(str(price2)) 
        print("현재 이더리움의 가격은", price2, "입니다.")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()