from random import randint
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtSql
from ui_mainWindow import Ui_MainWindow
from ui_PlayerWindow import Ui_Form

class Player:
    def __init__(self, name, icon, budget, current_bet) -> None:
        self.name = name
        self.icon = icon
        self.budget = budget
        self.current_bet = current_bet
    

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ID = 0
        # self.btn_ReloadQss.clicked.connect(load)
        self.btn_qss_reload.clicked.connect(load_dark_mode)
        self.btn_qss_reload_weird.clicked.connect(load_white_mode)
        
        self.playerlist = [None, None]

        self.btn_Create_Player_1.clicked.connect(self.ID1)
        self.btn_Create_Player_2.clicked.connect(self.ID2)
        self.sl_player1.valueChanged.connect(self.sl_val_change)
        self.sl_player1.setMinimum(0)
        self.set_player(1,randint(100, 10000), 'David', 'X')

#lb_outputField

    def sl_val_change(self):
        self.lb_outputField.setText(str(self.sl_player1.value()))

    def ID1(self):
        self.create_new_player(1)

    def ID2(self):
        self.create_new_player(2)        

    def create_new_player(self, ID:int):
        frm_addPlayer.reset_values()
        frm_addPlayer.showWindow(ID)

    def set_player(self, playerid:int, budget, name, icon):
        if playerid in range(1,3) and str(budget).isdigit():
            eval(f"self.sl_player{playerid}.setMaximum(int(budget))")
            eval(f"self.lb_Player{playerid}_budget.setText('Budget: '+str(budget))")
            eval(f"self.lb_Player{playerid}_name.setText('Name: '+str(name))")
            eval(f"self.lb_Player{playerid}_icon.setText('Icon: '+str(icon))")
        
            self.playerlist[playerid-1] = Player(name, icon, budget, 0)


class AddPlayerWindow(QMainWindow, Ui_Form):
    def __init__(self, parentWindow: MainWindow):
        super().__init__()
        self.setupUi(self)
        # load()
        self.parentWindow = parentWindow
        # self.btn_ReloadQss.clicked.connect(load)
        self.btn_commitNewPlayer.clicked.connect(self.commit_player)
        self.current_player:int = 0

    def reset_values(self):
        self.lnedit_icon.setText("")
        self.lnedit_playerName.setText("")
        self.lnedit_budget.setText("")
    

    def showWindow(self, player_id: int):
        self.current_player = player_id
        if player_id in range(1,3):
            self.show()

    def commit_player(self):
        self.hide()
        print('Budget',self.lnedit_budget.text())
        budget = self.lnedit_budget.text()
        name = self.lnedit_playerName.text()
        icon = self.lnedit_icon.text()
        self.parentWindow.set_player(self.current_player, budget, name, icon)

    
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
    frm_main = MainWindow()
    frm_addPlayer = AddPlayerWindow(parentWindow= frm_main)
    load_dark_mode()
    frm_addPlayer.hide()
    frm_main.show()
    app.exec()
