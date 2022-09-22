from player import Player
from gesture import Gesture
from random import choice
class AI(Player):
    def __init__(self):
        super().__init__()
        self.name = 'AI'
        

    def take_in_gestures(self):
        self.choice_of_gesture = choice(self.gestures)
        print(f'{self.name} has chosen {self.choice_of_gesture}')
        
    def take_in_gesture_update(self):
        self.gesture = Gesture()
        self.choice_of_gesture = choice(self.gesture.gestures_list)
        print(f'{self.name} has chosen {self.choice_of_gesture}')

