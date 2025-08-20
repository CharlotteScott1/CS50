"""
Tic Tac Toe Player
"""

import math
import copy

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
    Returns player who has the next turn on a board.   :)
    """
    xCount = 0
    oCount = 0
    for row in board:
        for space in row:
            if space == X: xCount += 1
            elif space == O: oCount += 1

    if oCount < xCount: return O
    else: return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.  :)
    """
    available = []
    for i,row in enumerate(board):
        for j,space in enumerate(row):
            if space == EMPTY:
                available += [(i,j)]

    return available


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newState = copy.deepcopy(board)
    if newState[action[0]][action[1]] != EMPTY: raise NameError("Action Invalid")
    else:
        newState[action[0]][action[1]] = player(newState)
        return newState

def winner(board):
    """
    Returns the winner of the game, if there is one.  :)
    """
    lineCountV = 0
    lineCountH = 0
    for player in (X,O):
        for i in range(len(board)):
            for j in range(len((board[i]))):
                if board[i][j] == player: lineCountH += 1
                if board[j][i] == player: lineCountV += 1
            if lineCountH == 3 or lineCountV == 3: return player
            lineCountH = 0
            lineCountV = 0
        if board[1][1] == player:
            if (board[0][0] == player and board[2][2] == player) or (board[2][0] == player and board[0][2] == player):
                return player
    return None




def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None: return True
    for row in board:
        for space in row:
            if space == EMPTY: return False
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    won = winner(board)
    if won == X : return 1
    elif won == O: return -1
    else: return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal (board)== True: return None

    def recursion(board, count):
        score = {"1":[],"0":[],"-1":[]}
        if winner(board) == None and terminal(board) == False:
            moves = actions(board)
            for move in moves:
                s, _ ,count = (recursion(result(board, move), count + 1))
                score[str(s)].append(move)
                if len(score["1"]) > 0 and len(score["0"]) > 0 and len(score["-1"]) > 0:
                    break
            if player(board) == X:
                if len(score["1"]) >0:
                    return 1, score["1"][0],count-1
                elif len(score["0"]) > 0:
                    return 0, score["0"][0], count-1
                else:
                    return -1, score["-1"][0], count-1
            else:
                if len(score["-1"]) >0:
                    return -1, score["-1"][0], count-1
                elif len(score["0"]) > 0:
                    return 0, score["0"][0], count-1
                else:
                    return 1, score["1"][0],count-1

        else:
            points = utility(board)
            return points, (0,0), count-1

    return recursion(board, 0)[1]
