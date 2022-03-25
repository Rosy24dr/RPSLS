from player import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()
        self.ai_randome = random.choice(self.gestures)
    
    
    def choose_gestures(self):
        return super().choose_gestures()
    
    
    
    
    #def ai_random(self):
        #random_gesture = random.choice(self.gestures)
        #print(f'AI has picked the {random_gesture} gesture.')
        


# my_ai = Ai()
# my_ai.ai_random()