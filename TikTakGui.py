from gettext import gettext
from stringprep import in_table_d1
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtSql
from ui_mainWindow import Ui_MainWindow
from ui_PlayerWindow import Ui_Form
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ID = 0
        # self.btn_ReloadQss.clicked.connect(load)
        self.btn_qss_reload.clicked.connect(load_dark_mode)
        self.btn_qss_reload_weird.clicked.connect(load_white_mode)
        
        self.btn_Create_Player_1.clicked.connect(self.ID1)
        self.btn_Create_Player_2.clicked.connect(self.ID2)
        


    def ID1(self):
        self.create_new_player(1)

    def ID2(self):
        self.create_new_player(2)        

    def create_new_player(self, ID:int):
        print(ID)
        text = ID
        frm_addPlayer.lnedit_budget.setText("Guthaben: ")
        frm_addPlayer.lb_Player_Number.setText(str(text))
        frm_addPlayer.show()

    
    

class PlayerWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # load()
        # self.btn_ReloadQss.clicked.connect(load)
        self.btn_commitNewPlayer.clicked.connect(self.commit_player)

    def commit_player(self):
        Player_ID = (frm_addPlayer.lb_Player_Number.text())
        frm_addPlayer.hide()
        print(self.lnedit_budget.text())
        print(frm_addPlayer.lb_Player_Number.text())
        if str(frm_addPlayer.lnedit_budget.text()) != str(frm_main.label_4.text):
            frm_main.lb_Player4_budget.setText(frm_addPlayer.lnedit_budget.text()) ## Idee: lb_Player(Player_ID) soll ein modulares System geben

    
    def exit_new_player(self):
        self.hide()

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
    frm_addPlayer.hide()
    frm_main.show()
    app.exec()
