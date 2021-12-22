from Player import Player
class Gameboard():
    def __init__(self, p1_name:str='Alice', p2_name:str = 'Bob', field_size:tuple[int] = (3,3)):
        self.field_size = field_size
        self.players = [Player(p_name=p1_name),Player(p_name=p2_name)]
        
        self.positions = {i+1:' ' for i in range(field_size[0]*field_size[1])}
    
    def redraw(self):
        self.board = [[] for i in range(self.field_size[0])]
        for i in range(self.field_size[1]):
            for j in range(self.field_size[0]):
                self.board[i].append(str(self.positions[(i+1)*(j+1)] + ('|' if j!=self.field_size[0]-1 else '')))
                
        print('\n'.join([''.join(i) for i in self.board])) 

    def new_draw(self):
        for player in self.players:
            # new_pos = (1,2)
            new_pos = player.draw() # (1,2) -> field 4; (2,3) -> field 8
            icon = player.icon
            print(new_pos[0]+(new_pos[1]-1)*self.field_size[0])
            self.positions[new_pos[0]*self.field_size[0]+(new_pos[1]-1)] = icon
            print(self.positions)
            self.redraw()
            
if __name__ == '__main__':
    g = Gameboard()
    g.redraw()
    g.new_draw()


#  | |X
# |||
# |||