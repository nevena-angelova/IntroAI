"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    if x_count > o_count:
        return O
    elif x_count < o_count:
        return X
    else:
        return X if x_count + o_count < 9 else None 

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    return {(i, j) for i in range(3) for j in range(3) if board[i][j] is EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if not is_action_valid(board, action):
        raise ValueError("Invalid action")
    
    new_board = [row[:] for row in board]  # Create a copy of the board
    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]
        
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not EMPTY:
            return board[0][col]
        
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    if all(cell is not EMPTY for row in board for cell in row):
        return True
    
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    max_action = max(actions(board), key=lambda action: min_value(result(board, action)))
    min_action = min(actions(board), key=lambda action: max_value(result(board, action)))

    if player(board) == X:
        return max_action
    else:
        return min_action

def min_value(board):
    """
    Returns the minimum value of the board.
    """
    if terminal(board):
        return utility(board)
    
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    
    return v

def max_value(board):
    """
    Returns the maximum value of the board.
    """
    if terminal(board):
        return utility(board)
    
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    
    return v



def is_action_valid(board, action):
    """
    Returns True if the action is valid on the board, False otherwise.
    """
    return 0 <= action[0] < 3 and 0 <= action[1] < 3 and board[action[0]][action[1]] is EMPTY
