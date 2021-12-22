class Player():
    def __init__(self, p_name:str):
        self.name = input('Wie heißt du?\n>')
        self.bet_value = 10
        self.budget = 0
        self.stuff = None
        self.icon = input('Choose your icon and you shall stick with it for ever: ')
    
    def set_budget(self):
        self.budget = input('Choose your budget and you shall stick with it for ever: ')
        try:
           self.budget = int(self.budget)
        except ValueError:
            self.budget = self.set_budget()
        return self.budget

    def bet(self):
        self.bet_value = input('place bet: ')
        try:
           self. bet_value = int(self.bet_value)
        except ValueError:
            self.bet_value = self.bet()
        if(self.bet_value > self.budget):
            print('you cannot set a bet higher than your budget')
            self.bet_value = self.bet()
        
        return self.bet_value

    def won(self)->int:
        self.budget += self.bet_value * 2
        return self.budget

    def draw(self, message:str=''):
        self.stuff = input(f'{message+": " if message else ""}{self.name}, in which spaces to you want to write your {self.icon}?\n> ')
        try:
            self.stuff = tuple([int(s.strip()) for s in self.stuff.split(',')])
        except ValueError:
            self.stuff = self.draw()
        return self.stuff



# board = [[' |', ' |', ' '], [' |', ' |', ' '], [' |', ' |', ' ']]
# positions = {1:' ', 2:'X', 3:' '}
if __name__ == '__main__':
    s1 = Player('Alice')
    print(s1.set_budget())
    print(s1.bet())
    print(s1.draw())
    print(s1.won())
    
#  1 2 3
# 1[][][]
# 2[][][]
# 3[][][]

# [] [x] []