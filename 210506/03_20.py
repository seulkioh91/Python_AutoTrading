# import sys
# from PyQt5.QtWidgets import *
# from PyQt5 import uic

# form_class = uic.loadUiType("mywindow.ui")[0]

# class MyWindow(QMainWindow, form_class):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.pushButton.clicked.connect(self.btn_clicked)
#         self.pushButton_2.clicked.connect(self.btn_clicked_2)

#     def btn_clicked(self):
#         print("매수")
#     def btn_clicked_2(self):
#         print("매도")

# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# app.exec_()