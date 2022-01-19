from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtSql
from ui_mainWindow import Ui_MainWindow
from ui_PlayerWindow import Ui_Form

class MainWindow(QMainWindow, Ui_MainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.btn_ReloadQss.clicked.connect(load)
        
        self.btn_Create_Player_1.clicked.connect(self.create_new_player)
        self.btn_Create_Player_2.clicked.connect(self.create_new_player)
        self.btn_qss_reload.clicked.connect(load_dark_mode)
        self.btn_qss_reload_weird.clicked.connect(load_white_mode)
        
    
    def create_new_player(self):
        frm_addPlayer.lnedit_budget.setText("Budget")
        frm_addPlayer.show()
        
class PlayerWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # load()
        # self.btn_ReloadQss.clicked.connect(load)
        self.btn_commitNewPlayer.clicked.connect(self.commit_player)
    
    def commit_player(self):
        frm_addPlayer.hide()
        print(self.lnedit_budget.text())
        
    
    def exit_new_player(self):
        self.hide()
    
    def player_commit(self):
        pass

def load_white_mode():
    frm_main.setStyleSheet(open('./stylesheet_main_white.qss', encoding="utf-8").read())
    frm_addPlayer.setStyleSheet(open('./stylesheet_addPlayer_white.qss', encoding="utf-8").read())

def load_dark_mode():
    frm_main.setStyleSheet(open('./stylesheet_main.qss', encoding="utf-8").read())
    frm_addPlayer.setStyleSheet(open('./stylesheet_addPlayer.qss', encoding="utf-8").read())
    
if __name__ == "__main__":
    app = QApplication()
    frm_addPlayer = PlayerWindow()
    frm_main = MainWindow()
    load_dark_mode()
    frm_main.show()
    app.exec()
