from player import Player
import random

class Ai(Player):
    def __init__(self):
        # self.ai = player
        super().__init__()
    
    def ai_random(self):
        random_gesture = random.choice(self.gestures)
        print(f'AI has picked the {random_gesture} gesture.')
        


my_ai = Ai()
my_ai.ai_random()