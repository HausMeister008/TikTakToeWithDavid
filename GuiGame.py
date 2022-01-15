from Player import * 
from Gameboard import *
from TikTakGui import *

class GuiGameboard(Gameboard):
    def __init__(self, players: list[str] = ['Alice', 'Bob'], f_size: int = 3):
        self.field_size = f_size
        self.players = []
        for p in range(2):
            chosen_icons = []
            for player in self.players:
                chosen_icons.append(player.icon)
            self.players.append(GuiPlayer(p_name=players[p], chosen_icons=chosen_icons))
        
        self.positions = {i+1:' ' for i in range(self.field_size**2)}
        self.playing = True
    
    def output(self, prompt):
        mainWindow.lb_outputField.setText(prompt)
        
class GuiPlayer(Player):
    def __init__(self, p_name: str, chosen_icons: list = ...):
        self.name = ""
        self.bet_value = 0
        self.budget = 0
        self.icon = ""
    
    def output(self, prompt):
        guiGameboard.output(prompt)
        
    def create_player(self, chosen_icons:list=[]):
        addPlayerWindow.show()
        """
        creating new Player by opening GUI input terminal
        """
     

def load():
    mainWindow.setStyleSheet(open('./stylesheet_main.qss', encoding="utf-8").read())
    addPlayerWindow.setStyleSheet(open('./stylesheet_addPlayer.qss', encoding="utf-8").read())
    
if __name__ == "__main__":
    app = QApplication()
    mainWindow = MainWindow()
    
    addPlayerWindow = PlayerWindow()
    mainWindow.btn_Create_Player_1.clicked.connect(
        mainWindow.create_new_player(window=addPlayerWindow)
        )
    mainWindow.btn_Create_Player_2.clicked.connect(
        mainWindow.create_new_player(window=addPlayerWindow)
        )
    guiGameboard = GuiGameboard()
    guiPlayer1 = GuiPlayer('Leon')
    guiPlayer2 = GuiPlayer('david')
    load()
    guiPlayer1.output("test")
    mainWindow.show()
    app.exec()