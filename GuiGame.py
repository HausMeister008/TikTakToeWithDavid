# next: getting main window to send return message to the gameboard after creating a new player 

# from tqdm import main
from csv import field_size_limit
from Player import * 
from Gameboard import *
from TikTakGui import *
from uiFiles.ui_mainWindow import *
import math
class MainWindow(MainWindow):
    def __init__(self):
        super().__init__()
        self.icon = "x"

    def get_player(self, id):
        """"
        returns single player when id given and all players when no id given
        """
        return (self.playerlist[id-1] if id-1<len(self.playerlist) else None) if (id or str(id).isdigit()) else self.playerlist
    
    def set_player(self, playerid:int, budget, name, icon):
        super().set_player(playerid, budget, name, icon)
            
    
  
# class SizeWindow(Ui_Dialog):
#     def __init__(self, fieldsize:MainWindow):
#         super(GuiGameboard).__init__()
#         self.width = int(3)
#         # GuiGameboard.field_size = self.field_size_maximum()

#     def field_size_maximum(self):
#         self.sl_field_size.value()
#         GuiGameboard.field_size = 5

class GuiGameboard(Gameboard):
    def __init__(self,mainWindow:MainWindow,playerWindow:MainWindow, players: list[str] = ['Alice', 'Bob']):
        # super(MainWindow).__init__()
        self.mainWindow = mainWindow
        self.playerWindow = playerWindow
        self.ui_field_size = field_size_limit
        self.field_size = mainWindow.sl_field_size.value()
        self.players = []
        for p in range(2):
            chosen_icons = []
            for player in self.players:
                chosen_icons.append(player.icon)
            self.players.append(GuiPlayer(gameBoard=self,playerWindow=self.playerWindow, p_name=players[p], chosen_icons=chosen_icons))
        
        self.positions = {i+1:' ' for i in range(self.field_size*self.field_size)}
        self.playing = True
    
    def reload_style_sheets(self):
        if toggle == 1:
            mainWindow.setStyleSheet(
                open("./stylesheet_main_white.qss", encoding="utf-8").read()
            )
            addPlayerWindow.setStyleSheet(
                open("./stylesheet_addPlayer_white.qss", encoding="utf-8").read()
            )
        else:
            mainWindow.setStyleSheet(open("./stylesheet_main.qss", encoding="utf-8").read())
            addPlayerWindow.setStyleSheet(
                open("./stylesheet_addPlayer.qss", encoding="utf-8").read()
            )
    
    def output(self, prompt):
        self.mainWindow.lb_outputField.setText(prompt)
    
    def get_player(self, id_):
        return self.mainWindow.get_player(id_) if (id_ or str(id_).isdigit()) else self.mainWindow.get_player()

    def create_player(self, id_):
        self.mainWindow.create_new_player(id_)

    def redraw(selfy):
        
        GuiGameboard.board = [[] for i in range(selfy.field_size)] # für 3x3 -> [[], [], []]
        for row in range(selfy.field_size):
            for column in range(selfy.field_size):
                pos = row*selfy.field_size + column + 1
                selfy.board[row].append(str(selfy.positions[pos]))
        selfy.mainWindow.draw(selfy.board)
        
class GuiPlayer(Player):
    def __init__(self,gameBoard:GuiGameboard, playerWindow, p_name: str, chosen_icons: list = ...):
        self.name = ""
        self.bet_value = 0
        self.budget = 0
        self.icon = ""
        self.gameBoard = gameBoard
        self.playerWindow = playerWindow
    
    def output(self, prompt):
        self.gameBoard.output(prompt)
        
    def create_player(self):
        """
        creating new Player by opening GUI input terminal
        """
        self.gameBoard.get_player()
      

def load():
    mainWindow.setStyleSheet(open('./stylesheet_main.qss', encoding="utf-8").read())
    addPlayerWindow.setStyleSheet(open('./stylesheet_addPlayer.qss', encoding="utf-8").read())
    
if __name__ == "__main__":
    app = QApplication()
    mainWindow = MainWindow()
    addPlayerWindow = AddPlayerWindow(parentWindow = mainWindow)
    guiGameboard = GuiGameboard(playerWindow=addPlayerWindow, mainWindow=mainWindow)
    mainWindow.btn_Create_Player_1.clicked.connect(lambda: guiGameboard.create_player(1))
    mainWindow.btn_Create_Player_2.clicked.connect(lambda: guiGameboard.create_player(2))
    guiPlayer1 = GuiPlayer(gameBoard=guiGameboard,playerWindow=addPlayerWindow, p_name='Leon')
    guiPlayer2 = GuiPlayer(gameBoard=guiGameboard, playerWindow=addPlayerWindow, p_name='david')
    # guiGameboard.redraw()
    mainWindow.show()
    load()
    app.exec()