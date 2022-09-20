from time import sleep
from player import Player
class Game:
    def __init__(self):
        self.player = Player()
        self.num_of_players = ''
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizzard', 'Spock']

    def display_welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spock.")
        sleep(1.5)
        print("Each match will be best of three games.")

    def how_many_players(self):
        play_game = False
        while play_game is False:
            self.num_of_players = input('How many Players? 1) for Human v AI 2) Human v Human: ')
            if self.num_of_players == '1':
                print('You have chosen a game for Human v AI')
                play_game = True
            elif self.num_of_players == '2':
                print('You have chosen a game for Human v Human')
                play_game = True
            else:                
                print("Please choose a correct game type. Let's try that again.")
                play_game = False
                
    def human_v_ai_game(self):


    def run_game(self):
        pass

    def display_gestures(self):
        pass
