from player import Player
from time import sleep
from gesture import Gesture

class Human(Player):
    def __init__(self, name):
        super().__init__()
        self.type = 'human'
        self.name = name

    def show_gestures(self):
        counter = 0
        print(f'{self.name}, please choose between the following options: ')
        for gesture in self.gestures:
            print(f'Choose {str(counter)} for {gesture}')
            sleep(1)
            counter += 1
            
            
    def take_in_gesture_update(self):
        self.show_gestures()
        self.gesture = Gesture()
        self.choice_of_gesture = self.gesture.pick_gesture()





    
