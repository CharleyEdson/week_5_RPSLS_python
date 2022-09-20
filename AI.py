from player import Player
from random import choice
class AI(Player):
    def __init__(self):
        super().__init__()
        self.name = 'AI'

    def ai_choose_gesture(self):
        self.choice_of_gesture = choice(self.gestures)
        print(f'{self.name} has chosen {self.choice_of_gesture}')
        


