# input is a list of strings
def rushhour(heuristic, rawInput):
    printBoard(rawInput)
    # print("right slide:")
    # printBoard(slideRight(2,3,rawInput))
    
    # print("left slide:")
    # printBoard(slideLeft(2,3,rawInput))
    print("slide up")
    slideUp(2,1,rawInput)
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
    rowToChange = board[posY] 
    charLabel = rowToChange[posX]
    for i in range(len(rowToChange)):
        if (rowToChange[i] == charLabel):
            rowToChange = swap(rowToChange, i - 1, i)
    board[posY] = rowToChange
    return board

#slide one step to the left with the X and Y position of leftmost element
def slideLeft(posX, posY, board):
    rowToChange = board[posY] 
    charLabel = rowToChange[posX]
    for i in range(len(rowToChange) - 2, -1, -1): # decrementing loop
        if (rowToChange[i] == charLabel):
            rowToChange = swap(rowToChange, i, i + 1)
    board[posY] = rowToChange
    return board

def slideUp(posX, posY, board):
    rowFirstEle = board[posY] 
    charLabel = rowFirstEle[posX]
    print(charLabel, " is Label")
    for i in range(6):
        temp = board[i]
        if (temp[posX] == charLabel):
            swapUp = board[i - 1]
            swapUp[posX] = charLabel
            temp[posX] = "-" 
            board[i - 1] = swapUp
            board[i] = temp
        printBoard(board)  
        print(i, " was above")         
    return 

def slideDown(posX, posY, board):
    return 

# calculate h(n) for blocking
