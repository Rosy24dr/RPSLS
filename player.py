


class Player: #list of gestures used in game 
    def __init__(self):
                        #index 0  index 1  index 2  index 3  index 4
        self.gestures = ['rock', 'paper', 'scissors','lizard', 'spock'] 
        self.selected_gesture = ""
        self.player_one = None
        self.player_two = None
       
    def choose_gestures(self):
        # return super().choose_gestures() 
        print('These are the gesture options:')
        gestures_list = ['Enter 0 for Rock.', 'Enter 1 for Paper.', 'Enter 2 for scissors',  'Enter 3 for Lizard', 'Enter 4 for spock.']
        for gestures in gestures_list:
            print(gestures)
        user_input = int(input('Enter a number from 0-4 to select your Gesture:'))
        print(f'You picked {self.gestures[user_input]}.')
        self.selected_gesture = self.gestures[user_input]


        
    
    # def score_keeper(self, score):
    #     self.player_one += score
    #     self.player_two += score
    #     return score
        

#my_gesture = Player()
#my_gesture.choose_gestures()

#print(my_gesture.selected_gesture)
    
#old one
# def game_gestures(self): #prompt to select gesture
    #     print(self.gestures)
    # user_input = int(input('Select your Gesture:'))

# # # how to call this page 
# my_game = Player()
# print(my_game.gestures[0]) 




#     def score_track(self,score): 
#         score = 0
#         while True:
#             if score == 1:
#                 print(f'Yay {self.name} you won this round')
#                 score += 1 
#                 self.score_track.append(score)
#                 return score
#             else:
#                 print(f'Oh no {self.name} you lost. Better luck next time.')

#         pass 

# my_player = Player()
# print(my_player.score_track(1))



  

     
# Player choices (Show choices and allow player to pick or AI random )
    # display all gesture options  - index and for loop to pull gesture
 
# Player choices (Show choices and allow player to pick or AI random )
    # display all gesture options  - index and for loop to pull gesture
    # display winner
# save result each turn- keep score
