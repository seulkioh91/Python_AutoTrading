from PyQt5.QtCore import *

class Worker(QThread):
    def run(self):
        while True:
            print("hi")
            self.sleep(1)