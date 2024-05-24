import math 
import random

class player:
    def __init__(self, letter):
        # letter is x or 0
        self.letter = letter

    # we want all polayer to get the next move given a game
    def get_move(self, game):
            pass

class RandomComputerPlay(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
         valid_square = False
         val = None
         while not valid_square:                          
              