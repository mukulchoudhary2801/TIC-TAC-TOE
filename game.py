class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # We will use a single list to rep 3x3 board
        self.curerent_winner = None # Keep tarck of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:  #slice board into three eual part 
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod   
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = [] 
        # for (i, spot) in enumerate(self.board):
        #     # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o']
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return len(self.available_moves())
    

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X' # Starting letter
    #  get the move over the appporiate player
    if letter == '0':
        square = o_player.get_move(game)
    else: 
        square = x_player.get_move(game)
    
    # let's define a function to make a move!
    if game.make_move(square, letter):
        if print_game
       
        