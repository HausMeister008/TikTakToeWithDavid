from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtSql
from frm_main import Ui_MainWindow


class Frm_main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.btn_ReloadQss.clicked.connect(load)
      
def load():
    frm_main.setStyleSheet(open('./stylesheet.qss', encoding="utf-8").read())
    

app = QApplication()
frm_main = Frm_main()
load()
frm_main.show()
app.exec()
