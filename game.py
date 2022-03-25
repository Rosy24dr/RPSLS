from human import Human
from player import Player
import time


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = Player()
        
    def display_welcome_message(self):
        print('Welcome to the Rock Paper, Scissors, Lizard and Spock Game')
        

    def display_rules(self): #displayig the rules 
        print('These are the rules:')
        rules_list = ['Rock crushes Scissors', 'Scissors cuts Paper', 'Paper covers Rock',
                      'Rock crushes Lizard', 'Lizard poisons Spock', 'Spock smashes Scissors',
                      'Scissors decapitates Lizard', 'Lizard eats Paper']
        for rules in rules_list:
            time.sleep(2.0)
            print(rules)
    
    def single_or_multi(self): #How to ask the user if they want multiplayer or single mode and print their input
        user_input = input('Please choose if single player or multiplayer mode. Enter single or multi:')
        while True: 
            if user_input == 'single':
                self.players_turn()

            elif user_input == 'multi':
                    self.players_turn()

            else: 
                user_input= input('Please try selection again:') 
                self.player_one.choose_gestures()

            return

    def players_turn(self): #asking the user if they want to go first or not
        user_input = input('Would you like to go first? Enter y/n:')
        if user_input == 'y':
            print('Ok, you will go first.')
            self.player_one.choose_gestures()
            print("Now it is player's two turn to pick:")
            self.player_two.choose_gestures()

        elif user_input == 'n':
            print('Player two will go first.')
            self.player_two.choose_gestures()
            print("Now it is player's one turn to pick:")
            self.player_one.choose_gestures()
        
        else: 
            user_input= input('Please try selection again:')
        
            
    def gesture_choice_comparison(self): #taking in the gesture choices and comparing them to pick a winner and incrementing the score
        while self.player_one.player_one_score < 3:
            if self.player_one.selected_gesture == self.player_two.selected_gesture:
                print("It is a tie")
                self.player_two.choose_gestures()

            elif self.player_one.selected_gesture == 'scissors':
                if  self.player_two.selected_gesture == 'paper'  or self.player_two.selected_gesture == 'spock' or self.player_two.selected_gesture == 'rock' or self.player_two.selected_gesture == 'lizard':
                    print('Player one wins this round. Let the next round begin.')
                    self.player_one.player_one_score += 1
                    self.player_two.choose_gestures()
                    self.gesture_choice_comparison()
                    self.player_one.player_one_score += 1
                    self.player_one.choose_gestures()
                    self.gesture_choice_comparison()
                    self.player_one.player_one_score += 1
                    return

            elif self.player_two.selected_gesture == 'scissors':
                if  self.player_one.selected_gesture == 'paper' or self.player_one.selected_gesture == 'spock' or self.player_one.selected_gesture == 'rock' or self.player_one.selected_gesture == 'lizard':
                    print('Player one wins this round. Let the next round begin.')
                    self.player_two.player_one_score += 1
                    self.player_one.choose_gestures()
                    self.gesture_choice_comparison()
                    self.player_two.player_one_score += 1
                    self.player_one.choose_gestures()
                    self.gesture_choice_comparison()
                    self.player_two.player_one_score += 1
                    return
                   
            
            elif self.player_one.selected_gesture == 'paper':
                if  self.player_two.selected_gesture == 'scissors'  or self.player_two.selected_gesture == 'spock' or self.player_two.selected_gesture == 'rock' or self.player_two.selected_gesture == 'lizard':
                    print('Player one wins this round. Let the next round begin.')
                    self.player_one.player_one_score += 1
                    self.player_two.choose_gestures()
                    self.gesture_choice_comparison()
                    self.player_one.player_one_score += 1
                    self.player_one.choose_gestures()
                    self.gesture_choice_comparison()
                    self.player_one.player_one_score += 1
                    return

            elif self.player_two.selected_gesture == 'paper':
                if  self.player_one.selected_gesture == 'scissors' or self.player_one.selected_gesture == 'spock' or self.player_one.selected_gesture == 'rock' or self.player_one.selected_gesture == 'lizard':
                    print('Player one wins this round. Let the next round begin.')
                    self.player_two.player_one_score += 1
                    self.player_one.choose_gestures()
                    self.gesture_choice_comparison()
                    self.player_two.player_one_score += 1
                    self.player_one.choose_gestures()
                    self.gesture_choice_comparison()
                    self.player_two.player_one_score += 1
                    return
            
            elif self.player_one.selected_gesture == 'rock':
                if  self.player_two.selected_gesture == 'paper'  or self.player_two.selected_gesture == 'spock' or self.player_two.selected_gesture == 'scissors' or self.player_two.selected_gesture == 'lizard':
                    print('Player one wins this round. Let the next round begin.')
                    self.player_one.player_one_score += 1
                    self.player_two.choose_gestures()
                    self.gesture_choice_comparison()
                    self.player_one.player_one_score += 1
                    self.player_one.choose_gestures()
                    self.gesture_choice_comparison()
                    self.player_one.player_one_score += 1
                    return

            elif self.player_two.selected_gesture == 'rock':
                if  self.player_one.selected_gesture == 'paper' or self.player_one.selected_gesture == 'spock' or self.player_one.selected_gesture == 'scissors' or self.player_one.selected_gesture == 'lizard':
                    print('Player one wins this round. Let the next round begin.')
                    self.player_two.player_one_score += 1
                    self.player_one.choose_gestures()
                    self.gesture_choice_comparison()
                    self.player_two.player_one_score += 1
                    self.player_one.choose_gestures()
                    self.gesture_choice_comparison()
                    self.player_two.player_one_score += 1
                    return

            elif self.player_one.selected_gesture == 'lizard':
                if  self.player_two.selected_gesture == 'paper'  or self.player_two.selected_gesture == 'spock' or self.player_two.selected_gesture == 'rock' or self.player_two.selected_gesture == 'scissors':
                    print('Player one wins this round. Let the next round begin.')
                    self.player_one.player_one_score += 1
                    self.player_two.choose_gestures()
                    self.gesture_choice_comparison()
                    self.player_one.player_one_score += 1
                    self.player_one.choose_gestures()
                    self.gesture_choice_comparison()
                    self.player_one.player_one_score += 1
                    return

            elif self.player_two.selected_gesture == 'lizard':
                if  self.player_one.selected_gesture == 'paper' or self.player_one.selected_gesture == 'spock' or self.player_one.selected_gesture == 'rock' or self.player_one.selected_gesture == 'scissors':
                    print('Player one wins this round. Let the next round begin.')
                    self.player_two.player_one_score += 1
                    self.player_one.choose_gestures()
                    self.gesture_choice_comparison()
                    self.player_two.player_one_score += 1
                    self.player_one.choose_gestures()
                    self.gesture_choice_comparison()
                    self.player_two.player_one_score += 1
                    return

            elif self.player_one.selected_gesture == 'spock':
                if  self.player_two.selected_gesture == 'paper'  or self.player_two.selected_gesture == 'scissors' or self.player_two.selected_gesture == 'rock' or self.player_two.selected_gesture == 'lizard':
                    print('Player one wins this round. Let the next round begin.')
                    self.player_one.player_one_score += 1
                    self.player_two.choose_gestures()
                    self.gesture_choice_comparison()
                    self.player_one.player_one_score += 1
                    self.player_one.choose_gestures()
                    self.gesture_choice_comparison()
                    self.player_one.player_one_score += 1
                    return

            elif self.player_two.selected_gesture == 'spock':
                if  self.player_one.selected_gesture == 'paper' or self.player_one.selected_gesture == 'scissors' or self.player_one.selected_gesture == 'rock' or self.player_one.selected_gesture == 'lizard':
                    print('Player one wins this round. Let the next round begin.')
                    self.player_two.player_one_score += 1
                    self.player_one.choose_gestures()
                    self.gesture_choice_comparison()
                    self.player_two.player_one_score += 1
                    self.player_one.choose_gestures()
                    self.gesture_choice_comparison()
                    self.player_two.player_one_score += 1
                    return
            return
    def display_winner(self): #displaying the winner based on the score
        if self.player_one.player_one_score > self.player_two.player_one_score:
            print ('Player one is the overall winner!!! Congrats!')
        else: 
            print('Player two is the overall winner!!! Congrats!')
        





