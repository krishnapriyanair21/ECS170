def hexapawn(board, boardSize, player, searchAhead):
    init = hexapawnGame(board, boardSize, player, searchAhead)
    #check = whiteMoveDown(init, 0, 0)
    # check = blackMoveUp(init, 2, 2)
    # check = blackDiagonalRight(init, 0, 0)
    check = whiteDiagonalLeft(init, 0, 1)
    # check = whiteDiagonalRight(init, 2, 1)
    # check = blackDiagonalLeft(init, 0, 0)
    print("initial board: ")
    print(init.board)
    print("new board: ")
    if (check):
        print(check)
    else:
        print("HAHA NOPE")
    return

class hexapawnGame(object):
    def __init__(self, board, size, player, searchAhead):
        self.board = board
        self.size = size
        self.player = player
        self.searchAhead = searchAhead
        self.score = None
    #board evaluation in class 
    def staticEval(self):
        # loop through board
            # count black and white pieces
        
        # set self.score = score and return it 
        return score

# move generator

#minimax search

def whiteMoveDown(currGame, posX, posY):
    board = (currGame.board).copy()
    # check that position is w
    if(board[posY][posX] != 'w'):
        print("Bad coordinates")
        return None
    # check if move possible
    if (board[posY + 1][posX] == '-'):
        # change current position to '-'
        changeToDash = list(board[posY]) 
        changeToDash[posX]= '-'
        # 'move' white down
        changeToChar = list(board[posY + 1])
        changeToChar[posX] = 'w'
        # convert to string
        changeToCharStr = ''.join(changeToChar)
        changeToDashStr = ''.join(changeToDash)
        # replace in board
        board[posY] = changeToDashStr
        board[posY + 1] = changeToCharStr
    else:
        return None
    return board

def blackMoveUp(currGame, posX, posY):
    board = (currGame.board).copy()
    # check that position is b
    if(board[posY][posX] != 'b'):
        print("Bad coordinates")
        return None
    # check if move possible
    if (board[posY - 1][posX] == '-'):
        # change current position to '-'
        changeToDash = list(board[posY]) 
        changeToDash[posX]= '-'
        # 'move' white down
        changeToChar = list(board[posY - 1])
        changeToChar[posX] = 'b'
        # convert to string
        changeToCharStr = ''.join(changeToChar)
        changeToDashStr = ''.join(changeToDash)
        # replace in board
        board[posY] = changeToDashStr
        board[posY - 1] = changeToCharStr
    else:
        return None
    return board

def whiteDiagonalRight(currGame, posX, posY):
    board = (currGame.board).copy()
    print("size: ", currGame.size)
    # check if current piece is w 
    if (board[posY][posX] != 'w'):
        return None
    if((posX + 1) >= currGame.size) or ((posY + 1) >= currGame.size):
        print("Out of range: White Diagonal Right")
        return None
    # check if right diagonal is in range
    # check if right diagonal is b

    return board

def whiteDiagonalLeft(currGame, posX, posY):
    board = (currGame.board).copy()
    # check if curr piece is w
    if (board[posY][posX] != 'w'):
        return None
    # check if left diagonal is in range
    if((posX - 1) < 0) or ((posY + 1) >= currGame.size):
        print("Out of range: White Diagonal Left")
        return None
    # check if left diagonal is b
    return board

def blackDiagonalRight(currGame, posX, posY):
    board = (currGame.board).copy()
    # check if curr piece is b
    # check if right diagonal is in range
    # check if right diagonal is w
    return board

def blackDiagonalLeft(currGame, posX, posY):
    board = (currGame.board).copy()
    # check if curr piece is b
    # check if left diagonal is in range
    # check if left diagonal is w 
    return board