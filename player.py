class Player: 
    def __init__(self):
                        #index 0  index 1  index 2  index 3  index 4
        self.gestures = ['rock', 'paper', 'scissors','lizard', 'spock'] 
        
          
    def game_gestures(self): 
        print(self.gestures)
    user_input = int(input('Select your Gesture:'))
 




    



my_game = Player()
print(my_game.gestures[0]) 




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
