from player import Player
from time import sleep

class Human(Player):
    def __init__(self):
        super().__init__()
        self.type = 'human'

    def show_gestures(self):
        counter = 0
        for gesture in self.gestures:
            print(f'Choose {str(counter)} for {gesture}')
            sleep(1)
            counter += 1