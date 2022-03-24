from player import Player 
from human import Human
from ai import Ai
import time


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None
       
       

    
    def display_welcome_message(self):
        print('Welcome to the Rock Paper, Scissors, Lizard and Spock Game')
        

    def display_rules(self): #displayig the rules with a 2.2 seconds delay
        print('These are the rules:')
        rules_list = ['Rock crushes Scissors', 'Scissors cuts Paper', 'Paper covers Rock',
                      'Rock crushes Lizard', 'Lizard poisons Spock', 'Spock smashes Scissors',
                      'Scissors decapitates Lizard', 'Lizard eats Paper']
        for rules in rules_list:
            time.sleep(2.0)
            print(rules)
    
    def single_or_multi(self): #How to ask the user if they want multiplayer or single mode and print thier input
        user_input = input('Please choose if single player or multiplayer mode. Enter single or multi:')
        if user_input == 'single':
            print(f'You picked {user_input} player mode.')
        else: 
            print(f'You picked {user_input} player mode.')
        

    def players_turn(self):
        user_input = input('Would you like to go first? Enter y/n:')
        if user_input == 'y':
            print('Ok, your will go first.')
            self.player.choose_gestures()
        else:
            print('Ai will go first.')
            self.player.choose_gestures()
       
        
    


    def display_winner(self):
        pass



my_game = Game()
my_game.display_welcome_message()
my_game.display_rules()
# # my_game.single_or_multi()
# # my_game.players_turn()
# my_game.human_choose_gestures()
