from ast import Break
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
        self.type_of_game = ''

    def run_game(self):
        self.display_welcome()
        self.how_many_players()
        self.decide_on_game(self.type_of_game)
        
        

    def display_welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spock.")
        sleep(1.5)
        print("Each match will be best of three games.")
        sleep(1)

    #This will decide on what type of game will be played, either human v human or human v AI.
    def how_many_players(self):
        play_game = False
        while play_game is False:
            self.num_of_players = input('How many Players? 1) for Human v AI 2) Human v Human: ')
            sleep(1)
            if self.num_of_players == '1':
                print('You have chosen a game for Human v AI')
                sleep(1)
                play_game = True
                self.type_of_game = 0
            elif self.num_of_players == '2':
                print('You have chosen a game for Human v Human')
                sleep(1)
                play_game = True
                self.type_of_game = 1
            else:                
                print("Please choose a correct game type. Let's try that again.")
                sleep(1)
                play_game = False
                

    def decide_on_game(self, game_type):
        if game_type == 0:
            self.player_one = Human('Player one')
            self.player_two = AI()
            self.player_v_player_game()
        if game_type == 1:
            self.player_one = Human('Player one')
            self.player_two = Human('Player two')
            self.player_v_player_game()




    
    def player_v_player_game(self):
        print('Use the number keys to enter your selection')
        sleep(1)
        while self.player_one.win_count <2 or self.player_two.win_count <2:
            self.player_one.show_gestures()
            self.player_one.take_in_gestures()
            print(f'{self.player_one.name} chose {self.player_one.choice_of_gesture}')
            sleep(1)
            if self.type_of_game == 0:
                self.player_two.ai_choose_gesture()
                self.game_rules_for_player_update(self.player_one.choice_of_gesture, self.player_two.choice_of_gesture)
            if self.type_of_game == 1:
                self.player_two.show_gestures()
                self.player_two.take_in_gestures()
                print(f'{self.player_two.name} chose {self.player_two.choice_of_gesture}')
                sleep(1)
                self.game_rules_for_player_update(self.player_one.choice_of_gesture, self.player_two.choice_of_gesture)
            print(f"{self.player_one.name}'s win count is {self.player_one.win_count}")
            sleep(1)
            print(f"{self.player_two.name}'s win count is {self.player_two.win_count}")
            sleep(1)
            if self.player_one.win_count >= 2:
                print(f'{self.player_one.name} is victorious')
                break
            if self.player_two.win_count >= 2:
                print(f'{self.player_two.name} is victorious')
                break


    def display_gestures(self):
        pass

    

    def game_rules_for_player_update(self,gesture_one, gesture_two):
        
        if gesture_one == gesture_two:
            sleep(1)
            print('Each player picked the same gesture, please re-pick.')
            self.player_one.win_count += 0
            self.player_two.win_count += 0

        #rock v scissors
        elif gesture_one == 'Rock' and gesture_two == 'Scissors':
            
            print('Rock Crushes Scissors')
            sleep(1)
            self.player_one.win_count += 1
        elif gesture_two == 'Rock' and gesture_one == 'Scissors':
            
            print('Rock Crushes Scissors')
            sleep(1)
            self.player_two.win_count += 1

        #scissors and paper
        elif gesture_one == 'Scissors' and gesture_two == 'Paper':
            
            print('Scissors cuts paper')
            sleep(1)
            self.player_one.win_count += 1
        elif gesture_two == 'Scissors' and gesture_one == 'Paper':
            
            print('Scissors cuts paper')
            sleep(1)
            self.player_two.win_count += 1

        #paper and rock
        elif gesture_one == 'Paper' and gesture_two == 'Rock':
            
            print('Paper covers Rock')
            sleep(1)
            self.player_one.win_count += 1
        elif gesture_two == 'Paper' and gesture_one == 'Rock':
            
            print('Paper covers Rock')
            sleep(1)
            self.player_two.win_count += 1
        #rock and lizard
        elif gesture_one == 'Rock' and gesture_two == 'Lizard':
            
            print('Rock crushes Lizard')
            sleep(1)
            self.player_one.win_count += 1
        elif gesture_two == 'Rock' and gesture_one == 'Lizard':
            
            print('Rock crushes Lizard')
            sleep(1)
            self.player_two.win_count += 1
        #lizard and spock
        elif gesture_one == 'Lizard' and gesture_two == 'Spock':
            
            print('Lizard poisons Spock')       
            sleep(1)     
            self.player_one.win_count += 1
        elif gesture_two == 'Lizard' and gesture_one == 'Spock':
            
            print('Lizard poisons Spock') 
            sleep(1)
            self.player_two.win_count += 1
        #spock and scissors
        elif gesture_one == 'Spock' and gesture_two == 'Scissors':
            
            print('Spock smashes Scissors')  
            sleep(1)          
            self.player_one.win_count += 1
        elif gesture_two == 'Spock' and gesture_one == 'Scissors':
            
            print('Spock smashes Scissors') 
            sleep(1)
            self.player_two.win_count += 1
        #scissors and lizard
        elif gesture_one == 'Scissors' and gesture_two == 'Lizard':
            print('Scissors decapitates Lizard') 
            sleep(1)           
            self.player_one.win_count += 1
        elif gesture_two == 'Scissors' and gesture_one == 'Lizard':
            print('Scissors decapitates Lizard') 
            sleep(1) 
            self.player_two.win_count += 1
        #lizard eats paper
        elif gesture_one == 'Lizard' and gesture_two == 'Paper':
            print('Lizard eats Paper')  
            sleep(1)          
            self.player_one.win_count += 1
        elif gesture_two == 'Lizard' and gesture_one == 'Paper':
            print('Lizard eats Paper')  
            sleep(1) 
            self.player_two.win_count += 1
        #paper disproves spock
        elif gesture_one == 'Paper' and gesture_two == 'Spock':
            print('Paper disproves Spock')   
            sleep(1)         
            self.player_one.win_count += 1
        elif gesture_two == 'Paper' and gesture_one == 'Spock':
            self.player_two.win_count += 1
            print('Paper disproves Spock')   
            sleep(1)
        #Spock vaporizes Rock
        elif gesture_one == 'Spock' and gesture_two == 'Rock':
            print('Spock vaporizes Rock')
            sleep(1)            
            self.player_one.win_count += 1
        elif gesture_two == 'Spock' and gesture_one == 'Rock':
            print('Spock vaporizes Rock')
            sleep(1) 
            self.player_two.win_count += 1
            