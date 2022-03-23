from player import Player

class Human(Player): 
    def __init__(self):
        self.choose_player = [1,2]
        super().__init__()
        0
    def choose_player(self):
        user_input = int(input('Press 1 for single, Press 2 for duo'))
        if user_input == self.choose_player[0]:
            print('Single Player')
        if user_input == self.choose_player[1]:
            print('Duo Battle')
     




player_one = Human()
print(player_one.choose_player)
