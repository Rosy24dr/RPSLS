from human import Human
from player import Player
from ai import Ai
import time


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = Player()
        
       

    
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
            self.players_two = Ai
            self.players_turn()
            #self.player_one.choose_gestures()
            #self.player_two.choose_gestures()
            
        else: 
            print(f'You picked {user_input} player mode.')
            #user_input = input('Would you like to go first? Enter y/n:')
            if user_input == 'y':
                self.player_two = Human
                self.players_turn()
                #self.player_one.choose_gestures()
                #self.player_two.choose_gestures()

    def players_turn(self):
        user_input = input('Would you like to go first? Enter y/n:')
        if user_input == 'y':
            print('Ok, your will go first.')
            self.player_one.choose_gestures()
            print('Now it is your turn to pick:')
            self.player_two.choose_gestures()

        elif user_input == 'n':
            print('Player two will go first.')
            self.player_two.choose_gestures()
            print('Now it is your turn to pick:')
            self.player_one.choose_gestures()
        
            
    # def gesture_choice(self):
    #    if self.player_one.choose_gestures == self.player_two.choose_gestures:
    #        print(f"{self.player_one} , {self.player_two} is a tie")
    #    elif self.player_one.choose_gestures == 'Rock':
    #         if self.player_two.choose_gestures == 'Scissors':
    #             print('Rock crushes Scissors')


    def display_winner(self):
        pass



my_game = Game()
# my_game.gesture_choice()
my_game.display_welcome_message()
my_game.display_rules()
my_game.single_or_multi()
# my_game.players_turn()

