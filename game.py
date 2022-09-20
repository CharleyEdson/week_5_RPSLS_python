from time import sleep
from player import Player
from human import Human
from AI import AI
class Game:
    def __init__(self):
        self.player = Player()
        self.num_of_players = ''
        self.player_one = ''
        self.player_two = ''
        self.ai_one = ''
        self.type_of_game = ''

    def run_game(self):
        self.display_welcome()
        self.how_many_players()
        self.decide_on_game(self.type_of_game)
        #self.test_up_to_now()
        

    def display_welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spock.")
        sleep(1.5)
        print("Each match will be best of three games.")

    #This will decide on what type of game will be played, either human v human or human v AI.
    def how_many_players(self):
        play_game = False
        while play_game is False:
            self.num_of_players = input('How many Players? 1) for Human v AI 2) Human v Human: ')
            if self.num_of_players == '1':
                print('You have chosen a game for Human v AI')
                play_game = True
                self.type_of_game = 0
            elif self.num_of_players == '2':
                print('You have chosen a game for Human v Human')
                play_game = True
                self.type_of_game = 1
            else:                
                print("Please choose a correct game type. Let's try that again.")
                play_game = False
                
    #This function instantiates the human or AI classes.            
    def decide_on_game(self, game_type):
        if game_type == 0:
            self.player_one = Human('Player one')
            self.ai_one = AI()
            self.human_v_ai_game()
        if game_type == 1:
            self.player_one = Human('Player one')
            self.player_two = Human('Player two')
            self.human_v_human_game()

    #This is a test function to check if everything is working up to date.
    def test_up_to_now(self):
        print(self.player_one.choice_of_gesture)

    #Need to still add in loop, and logic to determine which one wins
    def human_v_ai_game(self):
        print('Use the number keys to enter your selection')
        #sleep(.5)
        self.player_one.show_gestures()
        self.player_one.take_in_gestures()
        print(f'{self.player_one.name} chose {self.player_one.gestures[self.player_one.choice_of_gesture]}')
        self.ai_one.ai_choose_gesture()
        

    def human_v_human_game(self):
        pass

    def display_gestures(self):
        pass
