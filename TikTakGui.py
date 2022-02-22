from ast import Delete
from dataclasses import field
from mimetypes import init
from operator import truediv
from pickle import TRUE
from random import randint
from tkinter import CENTER
from tkinter.tix import COLUMN
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
    # QAlignCenter,
)
from PySide6.QtGui import QCursor
from PySide6.QtCore import Qt, Signal
from PySide6 import QtSql
from Gameboard import Gameboard
# from GuiGame import GuiGameboard, guiGameboard

from uiFiles.ui_mainWindow import Ui_MainWindow
from uiFiles.ui_addPlayerDialog import Ui_Dialog
from time import sleep


toggle = 0


class Player:
    def __init__(self, name, icon, budget, current_bet):
        self.name = name
        self.icon = icon
        self.budget = budget
        self.current_bet = current_bet



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        super(Gameboard).__init__()
        self.fieldsize = 0
        self.board = []
        self.setupUi(self)
        self.board = []
        self.ID = 1
        self.happened = False
        self.btn_qss_toggle.clicked.connect(lambda : self.switch_qss(MainWindow, AddPlayerWindow))
        self.btn_qss_toggle.setText("Whitemode")
        self.playerlist = [None, None]
        self.icon_storage= "x"
        self.sl_player1.setMinimum(0)
        self.sl_player2.setMinimum(0)
        self.total_budget = 0
        self.set_player(1, 100, "David", "I")
        self.set_player(2, 100, "Leon", "O")
        self.icon = "X"
        self.btn_render.clicked.connect(self.redraw)
        self.field_size = 3
        self.icon_counter = 0
        self.containing_frame = None
        self.sl_player1.valueChanged.connect(lambda: self.change_slider(1))
        self.sl_player2.valueChanged.connect(lambda: self.change_slider(2))
        self.lp_player1_sl_value.setText("Du musst noch setzen")
        self.lp_player2_sl_value.setText("Du musst noch setzen")
        

    def redraw(self):
        # if  (self.sl_field_size.value()% 2):
        #     self.field_size = self.sl_field_size.value()
        # else: self.field_size = self.sl_field_size.value() + 1
        self.field_size = self.sl_field_size.value() * 2 + 1

        positions = {i+1:' ' for i in range(self.field_size*self.field_size)}
        self.board = [[] for i in range(self.field_size)] # für 3x3 -> [[], [], []]
        row = 0 
        column = 0
        # self.already += 1
        for row in range(self.field_size):
            for column in range(self.field_size):
                posit = row*self.field_size + column + 1
                self.board[row].append(str(positions[posit]))
        self.draw(self.board)
    
    def draw(self, board: list):
        self.positions = {i+1:' ' for i in range(self.field_size*self.field_size)}
        if self.happened == 1:
            for b_index, column in enumerate(board):
                for index, button in enumerate(column):
                    self.gridLayout_2.removeWidget(self.containing_frame)
            

        for column in range(self.field_size):
            r = []
            for row in range(self.field_size):
                r.append(QPushButton(parent=self.fr_game_board, text=self.board[column][row]))
            board[column] = r
        self.happened = 1
        self.containing_frame = QFrame(self.fr_game_board)
        self.containing_frame.setStyleSheet("background: #00161e; min-height: 1px; min-width: 1px; ")
        self.containing_layout = QHBoxLayout(self.containing_frame)
        spacing = (10^(self.field_size * self.field_size))
        self.containing_layout.setSpacing(spacing)
        for b_index, column in enumerate(board):
            self.new_frame = QFrame(self.containing_frame)
            self.new_layout = QVBoxLayout(self.new_frame)
            self.new_layout.setSpacing(spacing * 4)
            for index, button in enumerate(column):
                self.board[b_index][index].setStyleSheet("font-size: 40px; font: arial; color: yellow; background: rgb(17,41,47); min-height: 1px;min-width: 1px; border: 0; margin: 0; padding: 0; border-radius: 5px; ")
                self.board[b_index][index].setCursor(QCursor(Qt.PointingHandCursor))
                self.board[b_index][index].setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
                x = self.board[b_index][index]
                x.clicked.connect(lambda checked=x.isChecked(), button=x, icon=self.icon: self.changeText(button, icon))
                self.new_layout.addWidget(board[b_index][index])
            self.containing_layout.addWidget(self.new_frame)
        self.containing_frame.setStyleSheet("background: hsl(192, 47%, 5%)")
        self.gridLayout_2.addWidget(self.containing_frame)
        
        self.board = board

    
    def change_slider(self, playerID):
        eval(f"self.lp_player{playerID}_sl_value.setText(str(self.sl_player{playerID}.value()))")

    def create_new_player(self, IDs: int):
        # addplayerWindow.reset_values()
        # addplayerWindow.showWindow(ID)
        dg = AddPlayerWindow()
        dg.setStyleSheet(open('./stylesheet_addPlayer.qss', encoding="utf-8").read())
        dg.clicked.connect(lambda name, icon, budget, ID=IDs: self.add_player(name=name, budget=budget, icon=icon, ID=IDs))
        dg.exec_()
        

    def add_player(self,**kwargs):
        # print('add player: ',kwargs)
        self.set_player(kwargs['ID'], kwargs['budget'], kwargs['name'], kwargs['icon'])

    def set_player(self, playerid: int, budget, name, icon):
        if playerid in range(1, 3) and str(budget).isdigit():
            tick_interval = int(budget / 10)
            eval(f"self.sl_player{playerid}.setMaximum(int(budget))")
            eval(f"self.sl_player{playerid}.setTickInterval(tick_interval)")
            eval(f"self.lb_Player{playerid}_budget.setText('Budget: '+str(budget))")
            eval(f"self.lb_Player{playerid}_name.setText('Name: '+str(name))")
            eval(f"self.lb_Player{playerid}_icon.setText('Icon: '+str(icon))")

            self.playerlist[playerid - 1] = Player(name, icon, budget, 0)


    def changeText(self, b: QPushButton, icon: str):
        if self.sl_player1.value() != 0:
            if self.sl_player2.value() != 0:
                self.icon_player_one = self.lb_Player1_icon.text()
                self.icon_player_two = self.lb_Player2_icon.text()
                if b.text() == " ":
                   if self.icon_storage == self.lb_Player1_icon.text():
                       self.icon_storage = self.lb_Player2_icon.text()
                   else:
                        self.icon_storage = self.lb_Player1_icon.text()
                   b.setText(self.icon_storage.replace("Icon: ", ""))
                self.evaluate()    
                self.icon_counter +=1

    def check_sym_num(self, sym_num, player)->bool:
        if sym_num == int(self.field_size):
            self.total_budget = int(self.lb_Player2_budget.text().strip("Budget: ")) + int(self.lb_Player1_budget.text().strip("Budget: "))
            self.lb_outputField.setStyleSheet("color: red")
            if player.name == self.lb_Player1_name.text().strip("Name: "):
                player.budget = int(self.lb_Player1_budget.text().strip("Budget: ")) + self.sl_player2.value()
                self.lb_Player1_budget.setText('Budget: '+str(player.budget))
                self.sl_player1.setMaximum(player.budget)
                budgettwo = int(self.lb_Player2_budget.text().strip("Budget: ")) - self.sl_player2.value()
                self.lb_Player2_budget.setText("Budet: "+str(budgettwo))
                self.sl_player2.setMaximum(budgettwo)
                if int(self.lb_Player2_budget.text().strip("Budget: ")) <= 0:
                    self.lb_outputField.setText(self.lb_Player1_name.text().strip("Name: ")+ " hat verloren")
                
                # self.lb_Player2_budget.setText('Budget: '+int(keeper))
                
                
            #  def set_player(self, playerid: int, budget, name, icon):
                 
            if player.name == self.lb_Player2_name.text().strip("Name: "):
                player.budget = int(self.lb_Player2_budget.text().strip("Budget: ")) + self.sl_player1.value()
                self.lb_Player2_budget.setText('Budget: '+str(player.budget))
                self.sl_player2.setMaximum(player.budget)
                budgettwo = int(self.lb_Player1_budget.text().strip("Budget: ")) - self.sl_player2.value()
                self.lb_Player1_budget.setText("Budet: "+str(budgettwo))
                self.sl_player1.setMaximum(budgettwo)
                if int(self.lb_Player1_budget.text().strip("Budget: ")) <= 0:
                    self.lb_outputField.setText(self.lb_Player2_name.text().strip("Name: ")+ " hat verloren")
                
            self.lb_outputField.setStyleSheet("color: Red; Font: Arial;")
            self.lb_outputField.setText((player.name)+str(" has won") )
            self.cleanup()
            self.playing = False
            print(self.total_budget)
            if self.total_budget != int(self.lb_Player2_budget.text().strip("Budget: ")) + int(self.lb_Player1_budget.text().strip("Budget: ")):
                self.lb_outputField.setText("irgendwas is schief gelaufen, spieler addieren nicht auf")
        return sym_num == int(len(self.board))

    
    def cleanup(self):
        for row in range(self.field_size):
            for column in range(self.field_size):
                self.board[row][column].setText(" ")
        self.sl_player1.setValue(0)
        self.sl_player2.setValue(0)  
        
    def evaluate(self):
        self.field_size = int(len(self.board))
        for player in self.playerlist:
            current_icon = player.icon
            rows_symbol_counter = 0
            columns_symbol_counter = 0
            diag_symbol_counter = 0
            rev_diag_symbol_counter = 0
            for row in self.board:
                row = [item.text() for  item in row] # -> ['x','o','x']
                rows_symbol_counter = row.count(current_icon)
                if(self.check_sym_num(rows_symbol_counter, player)):
                    break
            
            for column in range(self.field_size):
                for row in range(self.field_size):
                    columns_symbol_counter += 1 if self.board[row][column].text() == current_icon else 0
                    # print(self.board[row][column].text())
                    # print(f'c:{column} - r:{row}: {columns_symbol_counter}')
                if(self.check_sym_num(columns_symbol_counter, player)):
                    break
                else: 
                    columns_symbol_counter = 0
                
            for column in range(self.field_size):
                diag_symbol_counter += 1 if self.board[column][column].text() == current_icon else 0
                if(self.check_sym_num(diag_symbol_counter, player)):
                    break
                else: 
                    columns_symbol_counter = 0
            
            for column in range(self.field_size):
                rev_diag_symbol_counter += 1 if self.board[column][(self.field_size - 1) - column].text() == current_icon else 0
                if(self.check_sym_num(rev_diag_symbol_counter, player)):
                    break
                else: 
                    columns_symbol_counter = 0
        


    def switch_qss(self, Ptw, Chw):
        btn = self.btn_qss_toggle
        if btn.text() == "Darkmode":
            self.setStyleSheet(open("./stylesheet_main.qss", encoding="utf-8").read())
            btn.setText("whitemode")
            # Chw.setStyleSheet(open("./stylesheet_addPlayer.qss", encoding="utf-8").read())
        else:
            self.setStyleSheet(open("./stylesheet_main_white.qss", encoding="utf-8").read())
            # Chw.setStyleSheet(open("./stylesheet_addPlayer_white.qss", encoding="utf-8").read())
            btn.setText("Darkmode")
class AddPlayerWindow(QDialog, Ui_Dialog):
    
    clicked = Signal(str, str, int,arguments=['name', 'icon', 'budget'])
    
    def __init__(self,*args, **kwargs):
        super().__init__()
        self.setupUi(self)
        # load()
        self.current_player: int = 0
        self.btn_commitNewPlayer.setDisabled(True)
        self.btn_commitNewPlayer.clicked.connect(self.commit_player)
        self.lnedit_playerName.textEdited[str].connect(self.unlock)
        self.lnedit_icon.textEdited[str].connect(self.unlock)
        self.lnedit_budget.textEdited[str].connect(self.unlock)

        
    def unlock(self):
        if len(self.lnedit_playerName.text()) and len(self.lnedit_icon.text()) and len(self.lnedit_icon.text())==1 and len(self.lnedit_budget.text()):
            self.btn_commitNewPlayer.setDisabled(False)
        else:
            self.btn_commitNewPlayer.setDisabled(True)
            
    # def showWindow(self, player_id: int):
    #     self.current_player = player_id
    #     if player_id in range(1, 3):
    #         self.show()

    def commit_player(self):
        budget = self.lnedit_budget.text()
        budget = int(budget) if budget.isdigit() else 0
        name = self.lnedit_playerName.text()
        icon = self.lnedit_icon.text()
        # self.parentWindow.set_player(self.current_player, budget, name, icon)
        self.clicked.emit(name, icon, budget)
        
        self.accept()

    def exit_new_player(self):
        self.hide()

if __name__ == "__main__":
    frm_main = MainWindow()
    frm_addPlayer = AddPlayerWindow(parentWindow=frm_main)
    frm_main.qss_change()
    frm_main.show()
    QApplication.exec()
