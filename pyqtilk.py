import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic



class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.win =  uic.loadUi(r"GUI\AnaMenu.ui")
        self.win.btYeni.clicked.connect(self.tiklandi)
        self.win.cmbMusteri.currentIndexChanged.connect(self.degisti)
        self.comboDoldur()
        self.initUI()
        
    def initUI(self):
        self.win.show()

    def comboDoldur(self): 
        for i in range(0,5):
            self.win.cmbMusteri.addItem("Musteri"+str(i),str(i))
    
    def tiklandi(self):
        print("buton çalıştı")

    def degisti(self):
        secilen = self.win.cmbMusteri.currentIndex()
        print(secilen)

          
    
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 

