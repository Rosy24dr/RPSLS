from player import Player

class Human(Player): 
    def __init__(self):
        self.choose_player = [1,2]
        super().__init__()
        
    def choose_player(self):
        user_input = int(input('Press 1 for single, Press 2 for duo'))
        if user_input == self.choose_player[0]:
            print('Single Player')
        if user_input == self.choose_player[1]:
            print('Duo Battle')
     




# player_one = Human()
# print(player_one.choose_player)

#    def single_or_multi(self): #How to ask the user if they want multiplayer or single mode and print thier input
#         user_input = print(input('Please choose if single player or multiplayer mode. Enter single or multi:'))
#         if user_input == 'single':
#             print(f'You picked {user_input} player mode.')
#         else: 
#             print(f'You picked {user_input} player mode.')
#         #Why is it only printing the user's input and not the rest
