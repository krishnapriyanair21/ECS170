def hexapawn(board, boardSize, player, searchAhead):
    init = hexapawnGame(board, boardSize, player, searchAhead)
    moveGenerator(init)
    # check = hexapawnGame(board,boardSize,player,searchAhead)
    #check = whiteMoveDown(init, 0, 0)
    # check = blackMoveUp(init, 2, 2)
    # check.board = blackDiagonalRight(init, 1, 2)
    # check.board = whiteDiagonalLeft(init, 2, 1)
    # check.board = whiteDiagonalRight(init, 0, 1)
    # check.board = blackDiagonalLeft(init, 1, 2)
    # print("initial board: ")
    # # init.printBoard()
    # print(init.score)
    # if (init.score > 0):
    #     print("score greater than 0")
    # # print("new board: ")
    # if (check.board):
    #     check.printBoard()
    # else:
    #     print("HAHA NOPE")
    # return

class MinMaxTree(object):
    def __init__(self, game):
        self.game = game ## game should be hexapawn object
        self.parent = None
        self.children = []
    
    # Sample found on stack overflow: https://stackoverflow.com/questions/1925246/declaring-empty-class-member-in-python
    def addChild(self, child):
        self.children.append(child)
        child.parent = self
class hexapawnGame(object):
    def __init__(self, board, size, player, searchAhead):
        self.board = board
        self.size = size
        self.player = player
        self.searchAhead = searchAhead
        self.score = self.staticEval()
        self.curr = player

    # static evaluation function which sets score for hexapawn game object
    # +(size * 5) if current player wins
    # -(size * 5) if opponent wins
    # else score is current player markers - opponent player markers
    def staticEval(self):
        blackMarkers = 0
        whiteMarkers = 0
        whiteLose = False
        blackLose = False
        rowOne = list(self.board[0])
        rowThree = list(self.board[2])
        for i in range(3):
            if rowOne[i] == 'b':
                print("black wins")
                whiteLose = True #BLACK WINS
        for i in range(3):
            if rowThree[i] == 'w':
                print("white wins")
                blackLose = True #WHITE WINS
        # loop through board and count pieces
        for i in range(self.size):
            for j in range(self.size):
                if (self.board[i][j] == 'b'):
                    blackMarkers += 1
                if (self.board[i][j] == 'w'):
                    whiteMarkers += 1
        if (self.player == 'w'):
            if(whiteLose):
                self.score = int(self.size)*(-5)
            elif (blackLose):
                self.score =  int(self.size)*5
            else:
                self.score = int(whiteMarkers - blackMarkers)
        else:
            if (blackLose):
                self.score =  int(self.size)*(-5)
            elif (whiteLose):
                self.score =  int(self.size)*5
            else:
                self.score = int(blackMarkers - whiteMarkers)
        return self.score

    # For debugging
    def printBoard(self):
        print("next player: ", self.curr)
        for i in range(self.size):
            print(self.board[i])
    
# move generator
# once all moves are found create new hexapawnGame objects and switch the curr player
def moveGenerator(currGame):
    if (currGame.curr == 'w'):
        white = findWhiteAndBlack(currGame, 'white')
        possibleStates = whiteStates(white,currGame)
        ## currGame.curr = 'b' 
        for i in range(len(possibleStates)):
            print("board ", i, ": ")
            possibleStates[i].printBoard()
        return possibleStates ## FIX THIS
    else:
        black = findWhiteAndBlack(currGame, 'black')
        currGame.curr = 'w'
        return black
#minimax search

# Finds all states for white player
# creates hexapawn object with new board and sets current (next) player to b
# returns list of possible states
def whiteStates(white,currGame):
    possibleStates = []
    for i in range(len(white)):
        down = whiteMoveDown(currGame, white[i][0], white[i][1])
        right = whiteDiagonalRight(currGame, white[i][0], white[i][1])
        left = whiteDiagonalLeft(currGame, white[i][0], white[i][1])
        if(down):
            downHex = hexapawnGame(down,currGame.size,currGame.player,currGame.searchAhead)
            downHex.curr = 'b'
            possibleStates.append(downHex)
        if(right):
            rightHex = hexapawnGame(right,currGame.size,currGame.player,currGame.searchAhead)
            rightHex.curr = 'b'
            possibleStates.append(rightHex)
        if(left):
            leftHex = hexapawnGame(left,currGame.size,currGame.player,currGame.searchAhead)
            leftHex.curr = 'b'
            possibleStates.append(leftHex)
    return possibleStates

## Finds all white/black markers on the board
## Returns a list of tuples with coordinates of player we are lookingToFind
def findWhiteAndBlack(currGame, lookingToFind):
    size = currGame.size
    board = currGame.board.copy()
    white = []
    black = []
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'w':
                white.append((j,i)) ## Coordinates in (x,y) format
            if board[i][j] == 'b':
                black.append((j,i)) ## Coordinates in (x,y) format
    if(lookingToFind == 'black'):
        return black
    elif (lookingToFind == 'white'):
        return white
    else:
        return None

## MOVEMENT FUNCTIONS: WHITE UP/RIGHT DIAGONAL/LEFT DIAGONAL
## MOVEMENT FUNCTIONS: BLACK DOWN/RIGHT DIAGONAL/LEFT DIAGONAL
def whiteMoveDown(currGame, posX, posY):
    board = (currGame.board).copy()
    # check that position is w
    if(board[posY][posX] != 'w'):
        print("Bad coordinates")
        return None
    # check if out of range
    if ((posY + 1) >= currGame.size):
        print("out of range: White move up")
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

def blackMoveUp(currGame, posX, posY):
    board = (currGame.board).copy()
    # check that position is b
    if(board[posY][posX] != 'b'):
        print("Bad coordinates")
        return None
    # check if out of range
    if ((posY - 1) < 0):
        print("Out of Range: Black Move up")
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