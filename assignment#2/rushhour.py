# input is a list of strings
def rushhour(heuristic, rawInput):
    printBoard(rawInput)
    # print("right slide:")
    # printBoard(slideRight(2,3,rawInput))
    
    # print("left slide:")
    # printBoard(slideLeft(2,3,rawInput))
    # print("slide up")
    # slideUp(2,1,rawInput)
    # printBoard(rawInput)
    print("slide down")
    slideDown(2,2,rawInput)
    # if (heuristic == 0):
    #     #send to blocking
    # if (heuristic == 1):
    #     #send to selfmade

def printBoard(board):
    for i in board:
        print(i)

def swap(curr, pos1, pos2):
    curr = list(curr)
    curr[pos1], curr[pos2] = curr[pos2], curr[pos1]
    print(curr)
    return ''.join(curr)

#slide one step to the right with the X and Y position of rightmost element
def slideRight(posX, posY, board):
    if (posX == 5):
        return
    rowToChange = board[posY] 
    charLabel = rowToChange[posX]
    for i in range(len(rowToChange)):
        if (rowToChange[i] == charLabel):
            rowToChange = swap(rowToChange, i - 1, i)
    board[posY] = rowToChange
    return board

#slide one step to the left with the X and Y position of leftmost element
def slideLeft(posX, posY, board):
    if (posX == 0):
        return
    rowToChange = board[posY] 
    charLabel = rowToChange[posX]
    for i in range(len(rowToChange) - 2, -1, -1): # decrementing loop
        if (rowToChange[i] == charLabel):
            rowToChange = swap(rowToChange, i, i + 1)
    board[posY] = rowToChange
    return board

#slide up one step with the X and Y position of uppermost element
def slideUp(posX, posY, board):
    if (posY == 0):
        return
    rowFirstEle = board[posY] 
    charLabel = rowFirstEle[posX]
    for i in range(6):
        searchString = list(board[i])
        if (searchString[posX] == charLabel):
            swapUp = list(board[i - 1])
            searchString[posX] = swapUp[posX]
            swapUp[posX] = charLabel
            swapUpStr = ''.join(swapUp)
            searchStringtoStr = ''.join(searchString)
            board[i - 1] = swapUpStr
            board[i] = searchStringtoStr
    return board

def slideDown(posX, posY, board):
    if (posY == 5):
        return
    rowFirstEle = board[posY] 
    charLabel = rowFirstEle[posX]
    for i in range(5, 0, -1):
        searchString = list(board[i])
        if (searchString[posX] == charLabel):
            print( i , " found ", charLabel)
            swapDown = list(board[i + 1])
            searchString[posX] = swapDown[posX]
            swapDown[posX] = charLabel
            swapDownStr = ''.join(swapDown)
            searchStringtoStr = ''.join(searchString)
            board[i + 1] = swapDownStr
            board[i] = searchStringtoStr
        print ( "level ", i)
        printBoard(board)
    return board 

# calculate h(n) for blocking
