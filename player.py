


class Player: #list of gestures used in game 
    def __init__(self):
                        #index 0  index 1  index 2  index 3  index 4
        self.gestures = ['rock', 'paper', 'scissors','lizard', 'spock'] 
        self.selected_gesture = ""
        self.player_one = None
        self.player_two = None
        self.player_one_score = 0 
        self.player_two_score = 0
       
#As a developer, I want to store all of the gesture options/choices in a list. I want to find a way to utilize the list of gestures within my code (display gesture options, assign player a gesture, etc).
    def choose_gestures(self): 
        print('These are the gesture options:')
        gestures_list = ['Enter 0 for Rock.', 'Enter 1 for Paper.', 'Enter 2 for scissors',  'Enter 3 for Lizard', 'Enter 4 for spock.']
        for gestures in gestures_list:
            print(gestures)
        user_input = int(input('Enter a number from 0-4 to select your Gesture:'))
        print(f'You picked {self.gestures[user_input]}.')
        self.selected_gesture = self.gestures[user_input]

