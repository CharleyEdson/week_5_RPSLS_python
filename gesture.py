
from time import sleep

class Gesture:
    def __init__(self) -> None:
        self.name = ''
        self.gestures_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.picked_gesture = ''


    def pick_gesture(self):
        correct_choice = False
        while correct_choice is False:
            num_choice = int(input('Choose your gesture: '))
            sleep(1)
            if num_choice == 0 or num_choice == 1 or num_choice == 2 or num_choice == 3 or num_choice == 4:
                self.picked_gesture = self.gestures_list[num_choice]
                correct_choice = True
            else:
                print('You have chosen an incorrect key for a gesture. Please try again')
                sleep(1)
                correct_choice = False
        return self.picked_gesture
       




