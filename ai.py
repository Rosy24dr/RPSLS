from player import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()
        self.ai_random = random.choice(self.gestures)
    
    
    def choose_gestures(self):
        return super().choose_gestures()
    
    
    
    

        


