from Player import Player
class Gameboard():
    def __init__(self, p1_name:str='Alice', p2_name:str = 'Bob', field_size:tuple[int] = (3,3)):
        self.field_size = field_size
        self.players = [Player(p_name=p1_name),Player(p_name=p2_name)]
        
        self.positions = {i+1:' ' for i in range(field_size[0]*field_size[1])}
    
    def redraw(self):
        self.board = [[] for i in range(self.field_size[0])]
        for row in range(self.field_size[1]):
            for column in range(self.field_size[0]):
                pos = row*self.field_size[0] + column + 1
                self.board[row].append(str(self.positions[pos]) + ('|' if column!=self.field_size[0]-1 else ''))
                
        print('\n'.join([''.join(i) for i in self.board])) 

    def new_draw(self):
        for player in self.players:
            # new_pos = (1,2)
            new_pos = player.draw() # (1,2) -> field 4; (2,3) -> field 8
            icon = player.icon
            pos = new_pos[0]+(new_pos[1]-1)*self.field_size[0]
            self.positions[pos] = icon
            self.redraw()
            
if __name__ == '__main__':
    g = Gameboard()
    g.redraw()
    g.new_draw()
