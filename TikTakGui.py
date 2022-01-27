# button generator: spacing and growing

from mimetypes import init
from operator import truediv
from random import randint
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QFrame, QHBoxLayout, QSizePolicy
from PySide6.QtGui import QCursor
from PySide6.QtCore import Qt
from PySide6 import QtSql
from ui_mainWindow import Ui_MainWindow
from ui_PlayerWindow import Ui_Form


toggle = 0

class Player:
    def __init__(self, name, icon, budget, current_bet):
        self.name = name
        self.icon = icon
        self.budget = budget
        self.current_bet = current_bet
    
# class CustomButton(QPushButton):
#     def __init__():
#         super().__init__()
    
#     def setIcon(self, icon):
#         pass

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ID = 1
        # self.btn_ReloadQss.clicked.connect(load)
        self.btn_qss_reload.clicked.connect(reload_style_sheets)
        self.playerlist = [None, None]

        # self.btn_Create_Player_1.clicked.connect(lambda: self.create_new_player(1))
        # self.btn_Create_Player_2.clicked.connect(lambda: self.create_new_player(2)  )
        self.btn_qss_toggle.clicked.connect(load_stylesheet)
        # self.sl_player1.valueChanged.connect(self.sl_val_change)
        self.sl_player1.setMinimum(0)
        self.set_player(1,randint(100, 10000), 'David', 'X')
        self.set_player(2,randint(1, 200), "Leon", "O")
        self.icon = "X"
        self.childWindow = AddPlayerWindow

    def sl_val_change(self):
        self.lb_outputField.setText(str(self.sl_player1.value()))      

    def create_new_player(self,addplayerWindow:QMainWindow, ID:int): 
        addplayerWindow.reset_values()
        addplayerWindow.showWindow(ID)

    def set_player(self, playerid:int, budget, name, icon):
        if playerid in range(1,3) and str(budget).isdigit():
            eval(f"self.sl_player{playerid}.setMaximum(int(budget))")
            eval(f"self.lb_Player{playerid}_budget.setText('Budget: '+str(budget))")
            eval(f"self.lb_Player{playerid}_name.setText('Name: '+str(name))")
            eval(f"self.lb_Player{playerid}_icon.setText('Icon: '+str(icon))")
                    
            self.playerlist[playerid-1] = Player(name, icon, budget, 0)
    
    def draw(self, board:list):
        # print(board)
        for column in range(len(board)):
            r = []
            for row in range(len(board)):
                r.append(QPushButton(parent=self.fr_game_board, text=board[column][row]))
            board[column] = r
        
        containing_frame = QFrame(self.fr_game_board)
        containing_frame.setStyleSheet('min-height: 150px;min-width: 150px;max-height: 150px;max-width: 150px;')
        containing_layout = QHBoxLayout(containing_frame)
        containing_layout.setContentsMargins(0, 0, 0, 0)
        for b_index, column in enumerate(board):
            new_frame = QFrame(containing_frame)
            # new_frame.setStyleSheet('margin-left: 6px;')
            new_layout = QVBoxLayout(new_frame)
            new_layout.setContentsMargins(2,0,2,0)
            # .setSpacing(0)
            
            for index, button in enumerate(column):
                # print(b_index, index)
                sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
                board[b_index][index].setStyleSheet('min-height: 30px;min-width: 30px;max-height: 30px;max-width: 30px; border: 0; margin: 0; padding: 0; border-radius: 0;')
                board[b_index][index].setSizePolicy(sizePolicy)
                board[b_index][index].setCursor(QCursor(Qt.PointingHandCursor))
                
                if self.icon == "X":
                    self.icon = "C"
                else:
                    self.icon = "X"
                
                board[b_index][index].clicked.connect(lambda : board[b_index - 1][index - index].setText(self.icon_oscilator()))
                new_layout.addWidget(board[b_index][index])
                
            containing_layout.addWidget(new_frame)
        
        self.gridLayout_2.addWidget(containing_frame)

def reload_style_sheets():
    if toggle == 1:
        frm_main.setStyleSheet(open('./stylesheet_main_white.qss', encoding="utf-8").read())
        frm_addPlayer.setStyleSheet(open('./stylesheet_addPlayer_white.qss', encoding="utf-8").read())
    else:
        frm_main.setStyleSheet(open('./stylesheet_main.qss', encoding="utf-8").read())
        frm_addPlayer.setStyleSheet(open('./stylesheet_addPlayer.qss', encoding="utf-8").read())  
    
def toggle_stylesheet():
    if toggle == 0:
        frm_main.setStyleSheet(open('./stylesheet_main_white.qss', encoding="utf-8").read())
        frm_addPlayer.setStyleSheet(open('./stylesheet_addPlayer_white.qss', encoding="utf-8").read())
        frm_main.btn_qss_toggle.setText("Darkmode")
    else:
        frm_main.setStyleSheet(open('./stylesheet_main.qss', encoding="utf-8").read())
        frm_addPlayer.setStyleSheet(open('./stylesheet_addPlayer.qss', encoding="utf-8").read())
        frm_main.btn_qss_toggle.setText("Whitemode")
    
        
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
        print()
        budget = self.lnedit_budget.text()
        name = self.lnedit_playerName.text()
        icon = self.lnedit_icon.text()
        self.parentWindow.set_player(self.current_player, budget, name, icon)

    
    def exit_new_player(self):
        self.hide()
        
def load_stylesheet():
    text = frm_main.btn_qss_toggle.text()
    if text == "whitemode":
        frm_main.setStyleSheet(open('./stylesheet_main.qss', encoding="utf-8").read())
        frm_addPlayer.setStyleSheet(open('./stylesheet_addPlayer.qss', encoding="utf-8").read())
        frm_main.btn_qss_toggle.setText("darkmode")
    else:
        frm_main.setStyleSheet(open('./stylesheet_main_white.qss', encoding="utf-8").read())
        frm_addPlayer.setStyleSheet(open('./stylesheet_addPlayer_white.qss', encoding="utf-8").read())
        frm_main.btn_qss_toggle.setText("whitemode")
    
    
if __name__ == "__main__":
    app = QApplication()
    frm_main = MainWindow()
    frm_addPlayer = AddPlayerWindow(parentWindow= frm_main)
    frm_addPlayer.hide()
    # frm_main.setStyleSheet(open('./stylesheet_main.qss', encoding="utf-8").read())
    # frm_addPlayer.setStyleSheet(open('./stylesheet_addPlayer.qss', encoding="utf-8").read())
    load_stylesheet()
    frm_main.btn_qss_toggle.setText("Whitemode")
    # frm_main.reload_style_sheets()
    frm_main.show()
    app.exec()
