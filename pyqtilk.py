from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton
import sys
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton(text="deneme")
        
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    exe = App()
    sys.exit(app.exec_())
