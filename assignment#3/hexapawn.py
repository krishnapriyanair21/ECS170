## hexapawnGame object contains input elements: board, size, player, searchLevels
##                                              also contains score for each board and current player
## Static eval function in hexapawnGame object: automatically sets a value for each board 
##                                              which if overwrited in MinMax Search for higher levels
## MinMaxTree object contains: parent, children array, MAX/MIN level and hexapawn game object 

## Functions in rubric:
# minmaxSearch: line 137
# moveGenerator: line 122
# staticEval: line 61

def hexapawn(board, boardSize, player, searchAhead):
    init = hexapawnGame(board, boardSize, player, searchAhead)
    head = MinMaxTree(init)
    head.setMinOrMax()
    headNode = createMinMaxTree(head)
    bestChoice = minMaxSearch(headNode, searchAhead)
    if (bestChoice):
        return bestChoice.game.board
    else:
        return(init.board)

class MinMaxTree(object):
    def __init__(self, game):
        self.game = game # game should be hexapawn object
        self.parent = None
        self.children = []
        self.level = None # MIN or MAX
    
    # Sample found on stack overflow: https://stackoverflow.com/questions/1925246/declaring-empty-class-member-in-python
    def addChild(self, child):
        self.children.append(child)
        child.parent = self
    
    # Sets each max min game level based on parent
    def setMinOrMax(self):
        if (self.parent):
            if(self.parent.level == 'MAX'):
                self.level = 'MIN'
            else:
                self.level = 'MAX'
        else: # first level is None -> auto set to MAX
            self.level = 'MAX'

class hexapawnGame(object):
    def __init__(self, board, size, player, searchAhead):
        self.board = board # game board (INPUT)
        self.size = size # size of board (INPUT)
        self.player = player # which player we are (INPUT)
        self.searchAhead = searchAhead # how far search ahead (INPUT)
        self.score = self.staticEval() # evaluation function (Will change for higher levels of tree; func used for simplicity)
        self.curr = player # curr player 
        self.searchLevel = 0 # level of tree (altered in createMinMaxTree)
        
    # static evaluation function which sets score for hexapawn game object (taken from quiz 2)
    # +(size * 5) if current player wins
    # -(size * 5) if opponent wins
    # else score is (curr player clear markers - opponent clear markers) + 
    #               (curr player markers - opponent markers)
    # points for stalemate condition (win or lose if no possible states) done in whiteStates and blackStates
    def staticEval(self):
        blackMarkers = whiteMarkers = whiteClear = blackClear = 0
        whiteLose = blackLose = False
        rowOne = list(self.board[0])
        lastRow = list(self.board[self.size - 1])
        for i in range(self.size):
            if rowOne[i] == 'b':
                whiteLose = True #BLACK WINS
        for i in range(self.size):
            if lastRow[i] == 'w':
                blackLose = True #WHITE WINS

        # loop through board, count pieces, and add to black/white count 
        # if clear path add 1 point to black/white clear count
        for i in range(self.size):
            for j in range(self.size):
                if (self.board[i][j] == 'b'):
                    blackMarkers += 1
                    ## Find clear paths
                    clear = True
                    for k in range(0,i):
                        if(self.board[k][j] != '-'):
                            clear = False
                    if (clear == True):
                        blackClear += 1
                if (self.board[i][j] == 'w'):
                    whiteMarkers += 1
                    ## Find clear paths
                    clear = True
                    for k in range(i + 1,self.size):
                        if(self.board[k][j] != '-'):
                            clear = False
                    if (clear):
                        whiteClear += 1
        # Set scores according to above calculations
        if (self.player == 'w'):
            if(whiteLose):
                self.score = int(self.size)*(-5)
            elif (blackLose):
                self.score =  int(self.size)*5
            else:
                self.score = int(whiteClear - blackClear) + int(whiteMarkers - blackMarkers) 
        else:
            if (blackLose):
                self.score =  int(self.size)*(-5)
            elif (whiteLose):
                self.score =  int(self.size)*5
            else:
                self.score = int(blackClear - whiteClear) + int(blackMarkers - whiteMarkers)
        return self.score

    # For debugging
    def printBoard(self):
        print("next player:", self.curr)
        for i in range(self.size):
            print(self.board[i])
        print("score:",self.score)
    
# move generator
# uses helper functions to find all current player markers on board then all states for those markers
# returns all possible states for current player
def moveGenerator(currGame):
    if (currGame.curr == 'w'):
        white = findWhiteAndBlack(currGame, 'white')
        possibleStates = whiteStates(white,currGame)
    else:
        black = findWhiteAndBlack(currGame, 'black')
        possibleStates = blackStates(black,currGame)
    return possibleStates 


# minimax search
# uses tree created in createMinMax Tree: all possible states for provided depth
# recursively calls minmax until reaching last "row" of tree
# returns node with max score if parent is max
# returns node with min score if parent is min
def minMaxSearch(head, searchAhead):
    ## if searchLevel != 0 then call minMax with children 
    if (head.game.searchLevel < searchAhead - 1):
        if(head.children != []):
            for i in range(len(head.children)):
                if (head.children[i].game.score == int(head.children[i].game.size)*(-5)):
                    break # losing board no more games
                if (head.children[i].game.score == int(head.children[i].game.size)*(5)):
                    break  # winning board no more games
                minMaxSearch(head.children[i], searchAhead)
        else: # No possible game states on first call 
            return 
    if(head.level == 'MAX'):
        maxVal = head.game.size*(-5)
        maxGame = head.children[0]
        for i in range(len(head.children)):
            if (head.children[i].game.score > maxVal):
                maxGame = head.children[i]
                maxVal = head.children[i].game.score
        head.game.score = maxGame.game.score
        head.children.clear() ## remove list after searched
        return maxGame
    if(head.level == 'MIN'):
        minVal = head.game.size*(5)
        minGame = head.children[0]
        for i in range(len(head.children)):
            if(head.children[i].game.score < minVal):
                minGame = head.children[i]
                minVal = head.children[i].game.score
        head.game.score = minGame.game.score
        head.children.clear() ## remove list after searched
        return minGame

# creates the tree with all possible children 
# recursive call using searchAhead input
# returns root of tree to main
def createMinMaxTree(head):
    if(head.game.searchAhead > 0):
        nextLevel = moveGenerator(head.game)
        for i in range(len(nextLevel)):
            next = MinMaxTree(nextLevel[i])
            head.addChild(next)
            next.setMinOrMax()
            next.game.searchAhead = head.game.searchAhead - 1
            next.game.searchLevel = head.game.searchLevel + 1
        for j in range(len(head.children)):
            createMinMaxTree(head.children[j])
    elif (head.game.searchAhead == 0):
        return
    return head

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
    if (possibleStates == []):
        if (currGame.curr == currGame.player):
            currGame.score = int(currGame.size)*(-5)
        else:
            currGame.score = int(currGame.size)*(5)
    return possibleStates


# Finds all states for black player
# creates hexapawn object with new board and sets current (next) player to w
# returns list of possible states
def blackStates(black,currGame):
    possibleStates = []
    for i in range(len(black)):
        up = blackMoveUp(currGame, black[i][0], black[i][1])
        right = blackDiagonalRight(currGame, black[i][0], black[i][1])
        left = blackDiagonalLeft(currGame, black[i][0], black[i][1])
        if(up):
            upHex = hexapawnGame(up,currGame.size,currGame.player,currGame.searchAhead)
            upHex.curr = 'w'
            possibleStates.append(upHex)
        if(right):
            rightHex = hexapawnGame(right,currGame.size,currGame.player,currGame.searchAhead)
            rightHex.curr = 'w'
            possibleStates.append(rightHex)
        if(left):
            leftHex = hexapawnGame(left,currGame.size,currGame.player,currGame.searchAhead)
            leftHex.curr = 'w'
            possibleStates.append(leftHex)
    if (possibleStates == []):
        if (currGame.curr == currGame.player):
            currGame.score = int(currGame.size)*(-5)
        else:
            currGame.score = int(currGame.size)*(5)
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
## All movement functions check boundary cases and return altered board if possible; return None if no board possible
def whiteMoveDown(currGame, posX, posY):
    board = (currGame.board).copy()
    # check that position is w
    if(board[posY][posX] != 'w'):
        return None
    # check if out of range
    if ((posY + 1) >= currGame.size):
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
        return None
    # check if right diagonal is in range
    if((posX + 1) >= currGame.size) or ((posY + 1) >= currGame.size):
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
        return None

def whiteDiagonalLeft(currGame, posX, posY):
    board = (currGame.board).copy()
    # check if curr piece is w
    if (board[posY][posX] != 'w'):
        return None
    # check if left diagonal is in range
    if((posX - 1) < 0) or ((posY + 1) >= currGame.size):
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
        return None

def blackMoveUp(currGame, posX, posY):
    board = (currGame.board).copy()
    # check that position is b
    if(board[posY][posX] != 'b'):
        return None
    # check if out of range
    if ((posY - 1) < 0):
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
        return None
    # check if right diagonal is in range
    if ((posX + 1) >= currGame.size) or ((posY - 1) < 0):
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
        return None

def blackDiagonalLeft(currGame, posX, posY):
    board = (currGame.board).copy()
    # check if curr piece is b
    if (board[posY][posX] != 'b'):
        return None
    # check if left diagonal is in range
    if ((posX - 1) < 0) or ((posY + 1) < 0):
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
        return None