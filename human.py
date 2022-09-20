from player import Player
from time import sleep

class Human(Player):
    def __init__(self, name):
        super().__init__()
        self.type = 'human'
        self.name = name

    def show_gestures(self):
        counter = 0
        for gesture in self.gestures:
            print(f'Choose {str(counter)} for {gesture}')
            #sleep(1)
            counter += 1

    def take_in_gestures(self):
        self.choice_of_gesture = int(input('Choose your gesture: '))
        
