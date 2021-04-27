import sys
from PyQt5.QtWidgets import*
from PyQt5 import uic
from PyQt5.QtCore import*

form_class = uic.loadUiType("210427/bull.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        timer = QTimer(self)
        timer.start(5000)
        timer.timeout.connect(self.timeout)


    def timeout(self):
        print("5초예요")



app=QApplication(sys.argv)
window=MyWindow()
window.show()
app.exec_()