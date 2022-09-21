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
            sleep(1)
            counter += 1

    def take_in_gestures(self):
        correct_choice = False
        while correct_choice is False:
            num_choice = int(input('Choose your gesture: '))
            sleep(1)
            if num_choice == 0 or num_choice == 1 or num_choice == 2 or num_choice == 3 or num_choice == 4:
                self.choice_of_gesture = self.gestures[num_choice]
                correct_choice = True
            else:
                print('You have chosen an incorrect key for a gesture. Please try again')
                sleep(1)
                correct_choice = False
            
            





    
