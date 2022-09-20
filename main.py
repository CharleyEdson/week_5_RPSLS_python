from game import Game
from player import Player
from human import Human
from AI import AI


game_one = Game()
#game_one.run_game()
game_one.display_welcome()
game_one.how_many_players()
game_one.decide_on_game(0)
game_one.player_one.show_gestures()
game_one.player_one.take_in_gestures()


