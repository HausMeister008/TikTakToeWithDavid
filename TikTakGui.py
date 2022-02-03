from mimetypes import init
from operator import truediv
from random import randint
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QFrame,
    QHBoxLayout,
    QSizePolicy,
    QDialog,
    QInputDialog,
)
from PySide6.QtGui import QCursor
from PySide6.QtCore import Qt, Signal
from PySide6 import QtSql
from Gameboard import Gameboard

from uiFiles.ui_mainWindow import Ui_MainWindow
from uiFiles.ui_addPlayerDialog import Ui_Dialog


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
        self.icon_storage= "x"
        # self.btn_Create_Player_1.clicked.connect(lambda: self.create_new_player(1))
        # self.btn_Create_Player_2.clicked.connect(lambda: self.create_new_player(2)  )
        self.btn_qss_toggle.clicked.connect(load_stylesheet)
        self.sl_player1.setMinimum(0)
        self.set_player(1, randint(100, 10000), "David", "X")
        self.set_player(2, randint(1, 200), "Leon", "O")
        self.icon = "X"

    def create_new_player(self, addplayerWindow: QMainWindow, ID: int):
        # addplayerWindow.reset_values()
        # addplayerWindow.showWindow(ID)
        dg = addplayerWindow
        dg.accepted.connect(self.add_player)
        dg.show()

    def add_player(self, values):
        print(values)

    def set_player(self, playerid: int, budget, name, icon):
        if playerid in range(1, 3) and str(budget).isdigit():
            eval(f"self.sl_player{playerid}.setMaximum(int(budget))")
            eval(f"self.lb_Player{playerid}_budget.setText('Budget: '+str(budget))")
            eval(f"self.lb_Player{playerid}_name.setText('Name: '+str(name))")
            eval(f"self.lb_Player{playerid}_icon.setText('Icon: '+str(icon))")

            self.playerlist[playerid - 1] = Player(name, icon, budget, 0)

    def changeText(self, b: QPushButton, icon: str):
        self. icon_player_one = self.lb_Player1_icon.text()
        self.icon_player_two = self.lb_Player2_icon.text()
        if self.icon_storage == self.lb_Player1_icon.text():
                self.icon_storage = self.lb_Player2_icon.text()
        else:
            self.icon_storage = self.lb_Player1_icon.text()
        
        b.setText(self.icon_storage.replace("Icon: ", ""))

    def draw(self, board: list):
        # print(board)
        for column in range(len(board)):
            r = []
            for row in range(len(board)):
                r.append(
                    QPushButton(parent=self.fr_game_board, text=board[column][row])
                )
            board[column] = r

        containing_frame = QFrame(self.fr_game_board)
        containing_frame.setStyleSheet(
            "min-height: 150px;min-width: 150px;max-height: 150px;max-width: 150px;"
        )
        containing_layout = QHBoxLayout(containing_frame)
        containing_layout.setContentsMargins(0, 0, 0, 0)
        for b_index, column in enumerate(board):
            new_frame = QFrame(containing_frame)
            # new_frame.setStyleSheet('margin-left: 6px;')
            new_layout = QVBoxLayout(new_frame)
            new_layout.setContentsMargins(2, 0, 2, 0)
            # .setSpacing(0)

            for index, button in enumerate(column):
                # print(b_index, index)
                sizePolicy = QSizePolicy(
                    QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding
                )
                board[b_index][index].setStyleSheet(
                    "min-height: 10px;min-width: 20px;max-height: 30px;max-width: 30px; border: 0; margin: 0; padding: 0; border-radius: 0;"
                )
                board[b_index][index].setSizePolicy(sizePolicy)
                board[b_index][index].setCursor(QCursor(Qt.PointingHandCursor))

                if self.icon == "X":
                    self.icon = "O"
                else:
                    self.icon = "X"

                x = board[b_index][index]
                x.clicked.connect(
                    lambda checked=x.isChecked(), button=x, icon=self.icon: self.changeText(
                        button, icon
                    )
                )
                new_layout.addWidget(board[b_index][index])

            containing_layout.addWidget(new_frame)

        self.gridLayout_2.addWidget(containing_frame)


def reload_style_sheets():
    if toggle == 1:
        frm_main.setStyleSheet(
            open("./stylesheet_main_white.qss", encoding="utf-8").read()
        )
        frm_addPlayer.setStyleSheet(
            open("./stylesheet_addPlayer_white.qss", encoding="utf-8").read()
        )
    else:
        frm_main.setStyleSheet(open("./stylesheet_main.qss", encoding="utf-8").read())
        frm_addPlayer.setStyleSheet(
            open("./stylesheet_addPlayer.qss", encoding="utf-8").read()
        )


class AddPlayerWindow(QDialog, Ui_Dialog):
    
    accepted = Signal(dict)
    
    def __init__(self,*args, **kwargs):
        super().__init__()
        self.setupUi(self)
        # load()
        # self.btn_ReloadQss.clicked.connect(load)
        self.current_player: int = 0
        self.btn_commitNewPlayer.setDisabled(True)
        self.btn_commitNewPlayer.clicked.connect(self.commit_player)
        self.lnedit_playerName.textEdited[str].connect(self.unlock)
        self.lnedit_icon.textEdited[str].connect(self.unlock)
        self.lnedit_budget.textEdited[str].connect(self.unlock)
        

    def unlock(self):
        if self.lnedit_playerName.text() and self.lnedit_icon.text() and len(self.lnedit_icon.text()) and self.lnedit_budget.text():
            self.btn_commitNewPlayer.setDisabled(False)
        else:
            self.btn_commitNewPlayer.setDisabled(True)
            
    def showWindow(self, player_id: int):
        self.current_player = player_id
        if player_id in range(1, 3):
            self.show()

    def commit_player(self):
        budget = self.lnedit_budget.text()
        name = self.lnedit_playerName.text()
        icon = self.lnedit_icon.text()
        # self.parentWindow.set_player(self.current_player, budget, name, icon)
        values:dict = {
            'name': name, 
            'icon': icon,
            'budget': budget
        }
        print(values)
        self.accepted.emit(values)
        self.accept()

    def exit_new_player(self):
        self.hide()


def load_stylesheet():
    text = frm_main.btn_qss_toggle.text()
    if text == "darkmode":
        frm_main.setStyleSheet(open("./stylesheet_main.qss", encoding="utf-8").read())
        frm_addPlayer.setStyleSheet(
            open("./stylesheet_addPlayer.qss", encoding="utf-8").read()
        )
        frm_main.btn_qss_toggle.setText("whitemode")
    else:
        frm_main.setStyleSheet(
            open("./stylesheet_main_white.qss", encoding="utf-8").read()
        )
        frm_addPlayer.setStyleSheet(
            open("./stylesheet_addPlayer_white.qss", encoding="utf-8").read()
        )
        frm_main.btn_qss_toggle.setText("darkmode")


if __name__ == "__main__":
    app = QApplication()
    frm_main = MainWindow()
    frm_addPlayer = AddPlayerWindow(parentWindow=frm_main)
    frm_addPlayer.hide()
    # frm_main.setStyleSheet(open('./stylesheet_main.qss', encoding="utf-8").read())
    # frm_addPlayer.setStyleSheet(open('./stylesheet_addPlayer.qss', encoding="utf-8").read())
    load_stylesheet()
    frm_main.btn_qss_toggle.setText("Whitemode")
    # frm_main.reload_style_sheets()
    frm_main.show()
    app.exec()
