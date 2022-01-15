from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtSql
from ui_mainWindow import Ui_MainWindow
from ui_PlayerWindow import Ui_Form

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.btn_ReloadQss.clicked.connect(load)
    
    def create_new_player(self, window:QMainWindow):
        print(window.__class__)
        window.show()
        
        
class PlayerWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # load()
        # self.btn_ReloadQss.clicked.connect(load)
    
    def exit_new_player(self, window:QMainWindow):
        window.hide()
    
    def player_commit(self):
        pass
    
def load():
    frm_main.setStyleSheet(open('./stylesheet_main.qss', encoding="utf-8").read())
    frm_addPlayer.setStyleSheet(open('./stylesheet_addPlayer.qss', encoding="utf-8").read())
    
if __name__ == "__main__":
    app = QApplication()
    frm_main = MainWindow()
    frm_addPlayer = PlayerWindow()
    load()
    frm_main.show()
    app.exec()
