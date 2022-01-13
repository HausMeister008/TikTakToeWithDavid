from Player import Player, TTSSTTPlayer
import string
class Gameboard():
    def __init__(self, players:list[str]=['Alice', 'Bob'], f_size:int = 3):
        self.field_size = f_size
        self.players = []
        for p in range(2):
            chosen_icons = []
            for player in self.players:
                chosen_icons.append(player.icon)
            self.players.append(Player(p_name=players[p], chosen_icons=chosen_icons))
        
        self.positions = {i+1:' ' for i in range(self.field_size**2)}
        self.playing = True
        
    def redraw(self):
        self.board = [[] for i in range(self.field_size)] # für 3x3 -> [[], [], []]
        for row in range(self.field_size):
            for column in range(self.field_size):
                pos = row*self.field_size + column + 1
                self.board[row].append(str(self.positions[pos]) + ('|' if column!=self.field_size-1 else ''))
        self.board.append([string.ascii_uppercase[i] +( '|' if i!=self.field_size-1 else f'') for i in range(self.field_size)])
        print('\n'.join([''.join(i) for i in self.board])) 

    def new_draw(self):
        for player in self.players:
            # new_pos = (1,2)
            if self.playing:
                new_pos = player.draw(positions=self.positions) # (1,2) -> field 4; (2,3) -> field 8
                icon = player.icon
                pos = new_pos[0]+(new_pos[1]-1)*self.field_size
                self.positions[pos] = icon
                self.redraw()
                g.evaluate()
    
    def check_sym_num(self, sym_num, player)->bool:
        if sym_num == self.field_size:
            player.won()
            print(f"{player.name} has won!!!")
            self.playing = False
        return sym_num == self.field_size
    
    def evaluate(self):
        for player in self.players:
            current_icon = player.icon
            rows_symbol_counter = 0
            columns_symbol_counter = 0
            diag_symbol_counter = 0
            rev_diag_symbol_counter = 0
            
            for row in self.board:
                row = [item.replace('|','').strip() for  item in row] # -> ['x','o','x']
                rows_symbol_counter = row.count(current_icon)
                if(self.check_sym_num(rows_symbol_counter, player)):
                    break
            
            for column in range(self.field_size):
                for row in range(self.field_size):
                    columns_symbol_counter += 1 if self.board[row][column].replace('|','').strip() == current_icon else 0
                    # print(f'c:{column} - r:{row}: {columns_symbol_counter}')
                if(self.check_sym_num(columns_symbol_counter, player)):
                    break
                else: 
                    columns_symbol_counter = 0
                
            for column in range(self.field_size):
                diag_symbol_counter += 1 if self.board[column][column].replace('|','').strip() == current_icon else 0
                if(self.check_sym_num(diag_symbol_counter, player)):
                    break
                else: 
                    columns_symbol_counter = 0
            
            for column in range(self.field_size):
                rev_diag_symbol_counter += 1 if self.board[column][(self.field_size - 1) - column].replace('|','').strip() == current_icon else 0
                if(self.check_sym_num(rev_diag_symbol_counter, player)):
                    break
                else: 
                    columns_symbol_counter = 0
        
        if list(self.positions.values()).count(' ')>0:
            self.playing = True
            # print('Noone won! Game over!!!')
            
    

def define_f_size():
    try:
        return int(input('What size shall the field be?\n>'))
    except ValueError:
        define_f_size()

if __name__ == '__main__':
    f_size = define_f_size()
    g = Gameboard(f_size=f_size)
    g.redraw()
    # print(g.board)
    while g.playing:
        g.new_draw()
        
#Ideas to extend/change
#once a player has won the previous game, he may choose to overwrite one spot in the following game