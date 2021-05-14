def hexapawn(board, boardSize, player, searchAhead):
    init = hexapawnGame(board, boardSize, player, searchAhead)
    check = hexapawnGame(board,boardSize,player,searchAhead)
    #check = whiteMoveDown(init, 0, 0)
    # check = blackMoveUp(init, 2, 2)
    # check.board = blackDiagonalRight(init, 1, 2)
    # check.board = whiteDiagonalLeft(init, 2, 1)
    # check.board = whiteDiagonalRight(init, 0, 1)
    # check.board = blackDiagonalLeft(init, 1, 2)
    print("initial board: ")
    init.printBoard()
    init.staticEval()
    print("new board: ")
    if (check.board):
        check.printBoard()
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
        score = 0
        blackMarkers = 0
        whiteMarkers = 0
        rowOne = list(self.board[0])
        rowThree = list(self.board[2])
        for i in range(3):
            if rowOne[i] == 'b':
                print("black wins")
                return #BLACK WINS
        for i in range(3):
            if rowThree[i] == 'w':
                print("white wins")
                return #WHITE WINS
        # loop through board
            # count black and white pieces
        for i in range(self.size):
            for j in range(self.size):
                if (self.board[i][j] == 'b'):
                    blackMarkers += 1
                if (self.board[i][j] == 'w'):
                    whiteMarkers += 1
        print("White count: ", whiteMarkers)
        print("Black count: ", blackMarkers)
        # set self.score = score and return it 
        return score
    def printBoard(self):
        # for visual/debugging purposes
        print("current player: ", self.player)
        size = self.size
        for i in range(size):
            print(self.board[i])
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
    # check if current piece is w 
    if (board[posY][posX] != 'w'):
        print("white right diagonal curr pos is not w")
        return None
    # check if right diagonal is in range
    if((posX + 1) >= currGame.size) or ((posY + 1) >= currGame.size):
        print("Out of range: White Diagonal Right")
        return None
    # check if right diagonal is b
    if(board[posY + 1][posX + 1] == 'b'):
        changeToDash = list(board[posY])
        changeToDash[posX] = '-'
        changeToW = list(board[posY + 1])
        changeToW[posX + 1] = 'w'
        changeToDashStr = ''.join(changeToDash)
        changeToWStr = ''.join(changeToW)
        board[posY] = changeToDashStr
        board[posY + 1] = changeToWStr
        return board
    else: 
        print("WhiteRightDiagonal is not black")
        return None

def whiteDiagonalLeft(currGame, posX, posY):
    board = (currGame.board).copy()
    # check if curr piece is w
    if (board[posY][posX] != 'w'):
        print("White Diagonal Left curr pos is not w")
        return None
    # check if left diagonal is in range
    if((posX - 1) < 0) or ((posY + 1) >= currGame.size):
        print("Out of range: White Diagonal Left")
        return None
    # check if left diagonal is b
    if(board[posY + 1][posX - 1] == 'b'):
        changeToDash = list(board[posY])
        changeToDash[posX] = '-'
        changeToW = list(board[posY + 1])
        changeToW[posX - 1] = 'w'
        changeToDashStr = ''.join(changeToDash)
        changeToWStr = ''.join(changeToW)
        board[posY] = changeToDashStr
        board[posY + 1] = changeToWStr
        return board
    else: 
        print("WhiteLeftDiagonal is not black")
        return None

def blackDiagonalRight(currGame, posX, posY):
    board = (currGame.board).copy()
    # check if curr piece is b
    if (board[posY][posX] != 'b'):
        print("Black right diagonal curr pos is not b")
        return None
    # check if right diagonal is in range
    if ((posX + 1) >= currGame.size) or ((posY - 1) < 0):
        print("Out of Range: Black Diagonal Right")
        return None
    # check if right diagonal is w
    if (board[posY - 1][posX + 1] == 'w'):
        changeToDash = list(board[posY])
        changeToDash[posX] = '-'
        changeToW = list(board[posY - 1])
        changeToW[posX + 1] = 'b'
        changeToDashStr = ''.join(changeToDash)
        changeToWStr = ''.join(changeToW)
        board[posY] = changeToDashStr
        board[posY - 1] = changeToWStr
        return board
    else:
        print("Black Right Diagonal is not white")
        return None

def blackDiagonalLeft(currGame, posX, posY):
    board = (currGame.board).copy()
    # check if curr piece is b
    if (board[posY][posX] != 'b'):
        print("Black Diagonal Left curr pos is not b")
        return None
    # check if left diagonal is in range
    if ((posX - 1) < 0) or ((posY + 1) < 0):
        print("Out of range: Black Diagonal Left")
        return None
    # check if left diagonal is w 
    if(board[posY - 1][posX - 1] == 'w'):
        changeToDash = list(board[posY])
        changeToDash[posX] = '-'
        changeToW = list(board[posY - 1])
        changeToW[posX - 1] = 'b'
        changeToDashStr = ''.join(changeToDash)
        changeToWStr = ''.join(changeToW)
        board[posY] = changeToDashStr
        board[posY - 1] = changeToWStr
        return board
    else: 
        print("Black Left Diagonal is not white")
        return None
    return board