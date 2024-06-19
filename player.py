import math 
import random

class player:
    def __init__(self, letter):
        # letter is x or 0
        self.letter = letter

    # we want all polayer to get the next move given a game
    def get_move(self, game):
            pass

class RandomComputerPlayER(player):
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
            square = input(self.letter + '\'s turn. Input move (0-9):')
            # we're going to check that this is a correct value by trying to cast 
            # it to an integer, and if it's not then we say its invalid 
            # if that spot is not available on the board, we also say its invalid 
            try :
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, then yay!
            except ValueError:
                print('Invalid square. Try again.')
        return val

def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()

    letter =  'x' # Starting letter 
    # iterate while the game still has empty squares 
    # (we don't have to worry abou winner because we'll just return that 
    # which break the loop )
     
                    
              