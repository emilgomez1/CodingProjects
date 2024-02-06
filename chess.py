###
# Author: Emil Gomez
# Description: This program is a 2 player chess game, in which the players
# enter the index of their piece and if they want to move left or right.
# For each color there is one king and two knights.

###

from graphics import graphics

W_KNIGHT = 'WKn'
W_KING = 'WKi'
B_KNIGHT = 'BKn'
B_KING = 'BKi'
EMPTY = '   '
WHITE = 'White'
BLACK = 'Black'
LEFT = 'l'
RIGHT = 'r'

# This checks to see if the index that the player input, is
# valid. If it is valid it returns true.
# Board: This is the list of the pieces on the board.
# Position: This is the index that the player inputs to pick
# what piece they want to move.
# Player: This is used to check if the index that the player put
# is a piece of their color.
#
def is_valid_move(board, position, player):
    if 0 <= position <= 8:
        return player[0] == board[position][0]

    return False
# This is the function for the knights moves. This
# checks the direction that the player wants to move,
# and moves according to that direction
# Board: Checks the index of the board and if the index to where
# the piece is moving to is another piece then the other piece is removed.
# Position: This is used to check the pieces on the board list.
# Direction: two if statements according to where the player is moving.
def move_knight(board, position, direction):
    if direction == 'r':
        i = position
        if i <= 7:
            board[i+2] = board[i]
            board[i] = EMPTY
    if direction == 'l':
        i = position
        if i >= 2:
            board[i - 2] = board[i]
            board[i] = EMPTY

    ''' Implement. '''
# This function is almost the same as the knight function, but the king
# moves until there is a piece in front of it, and then it kills it.
# All the parameters in this function work the same as the knight function.
def move_king(board, position, direction):
    if direction == 'r':
        i = position
        while i < 8 and board[i+1] == EMPTY:
            board[i], board[i+1] = board[i+1], board[i]
            i += 1
        if i != 8:
            board[i + 1] = board[i]
            board[i] = EMPTY

    if direction == 'l':
        i = position
        while i > 0 and board[i - 1] == EMPTY:
            board[i], board[i - 1] = board[i - 1], board[i]
            i -= 1
        if i != 0:
            board[i - 1] = board[i]
            board[i] = EMPTY



    ''' Implement. '''
# This takes the board list that is updated every move, and prints it.
def print_board(board):
    string = ''
    for i in board:
        string += '| ' + i + ' '
    print('+-----------------------------------------------------+')
    print(string + '|')
    print('+-----------------------------------------------------+')
# This takes the updated board list but prints it onto a canvas. The gui
# parameter takes in the canvas size and title.
# The function goes through the board list and at each index it prints a box
# and prints the piece that is in that box.
def draw_board(board, gui):
    gui.clear()
    for i in range(len(board)):
        x_pos = i * 100
        text_x = x_pos + 25
        y = 130
        gui.rectangle(x_pos, 100, 100, 100, 'red')
        if board[i][0] == 'W':
            gui.text(text_x, y, board[i], 'White')
        elif board[i][0] == 'B':
            gui.text(text_x, y, board[i], 'Black')
        gui.line(x_pos, 100, x_pos, 200, 'black')
        gui.text(250, 30, '1 Dimensional Chess', 'green', 30)
    gui.update_frame(20)
    ''' Implement. '''
# This function checks the board list and if either the black or white
# king are gone than it announces the winner of the game. If none of the
# kings are gone then it returns false and the game continues.
def is_game_over(board):
    if W_KING not in board:
        print_board(board)
        print('Black wins!')
        exit()
    elif B_KING not in board:
        print_board(board)
        print('White wins!')
        exit()

    return False

# This checks the position that the player input, and if it is a knight,
# the knight function is called. If it the position is a king then the king
# function is called with all the parameters. 

def move(board, position, direction):
    if board[position] == W_KNIGHT or board[position] == B_KNIGHT:
        move_knight(board, position, direction)
    else:
        move_king(board, position, direction)


    ''' Implement. '''


def main():
    
    # Create the canvas
    gui = graphics(900, 200, '1 Dimensional Chess')

    # This is the starting board.
    # This board variable can and should be passed to other functions
    # and changed as moves are made.
    board = [W_KING, W_KNIGHT, W_KNIGHT, EMPTY, EMPTY, EMPTY, B_KNIGHT, B_KNIGHT, B_KING]
    
    # White typically starts in chess.
    # This will change between WHITE and BLACK as the turns progress.
    player = WHITE
    
    # This variable will be updated to be True if the game is over.
    # The game is over after one of the kings dies.
    is_game_won = False

    # This loop controls the repetitive nature of the turns of the game.
    while not is_game_won:
        
        print_board(board)

        # Draw the board
        draw_board(board, gui)

        position = int(input(player + ' enter index:\n'))
        direction = input(player + ' enter direction (l or r):\n')

        # If the desired move is valid, then call the move function.
        # Also, change the player variable.
        if is_valid_move(board, position, player):
            if player == WHITE:
                move(board, position, direction)
                player = BLACK
            else:
                move(board, position, direction)
                player = WHITE
            # Draw the board again
            draw_board(board, gui)
            is_game_won = is_game_over(board)

main()

