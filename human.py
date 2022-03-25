from player import Player

class Human(Player): 
    def __init__(self):
        super().__init__()

    def choose_gestures(self):
        return super().choose_gestures()
        # # return super().choose_gestures() 
        # print('These are the gesture options:')
        # gestures_list = ['Enter 0 for Rock.', 'Enter 1 for Paper.', 'Enter 2 for scissors',  'Enter 3 for Lizard', 'Enter 4 for spock.']
        # for gestures in gestures_list:
        #     print(gestures)
        # user_input = int(input('Enter a number from 0-4 to select your Gesture:'))
        # print(f'You picked {self.gestures[user_input]}.')
        # self.selected_gesture = self.gestures[user_input]


