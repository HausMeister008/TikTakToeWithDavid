from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtSql
from ui_mainWindow import Ui_MainWindow
from ui_PlayerWindow import Ui_Form

class Frm_main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.btn_ReloadQss.clicked.connect(load)
    
    def create_new_player(self):
        frm_addPlayer.show()
        
        
class Frm_PlayerWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # load()
        # self.btn_ReloadQss.clicked.connect(load)
    
    def exit_new_player(self):
        frm_addPlayer.hide()
    
    def player_commit(self):
        pass
    
def load():
    frm_main.setStyleSheet(open('./stylesheet_main.qss', encoding="utf-8").read())
    frm_addPlayer.setStyleSheet(open('./stylesheet_addPlayer.qss', encoding="utf-8").read())
    

app = QApplication()
frm_main = Frm_main()
frm_addPlayer = Frm_PlayerWindow()
load()
frm_main.show()
app.exec()
